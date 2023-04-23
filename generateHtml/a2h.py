# coding: utf-8
import requests
import datetime
import time
import oss2
import json
import inquirer
from bs4 import BeautifulSoup

"""
利用 BeautifulSoup 处理html
获取公众号文章内容
处理文章内图片上传到OSS中
生成文章列表的json文件上传到oss中
包含了测试和正式路径，以及文章的新增和删除
"""

bucket_name = 'bucket_name'
endpoint = 'endpoint'
auth = oss2.Auth('access_key_id', 'access_key_secret')
bucket = oss2.Bucket(auth, endpoint, bucket_name)
article_path = 'article_path'
host = 'host'

test_article_path = 'test_article_path'

isTest = False

# 模板html,微信抓取到的html内容过多.
T_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="icon" href="./favicon.ico">
    <meta charset="UTF-8">
    <meta name="referrer" content="never">
    <meta name="referrer" content="no-referrer">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content</title>
    <style>{style}</style>
</head>
<body>
    <div style='max-width: 677px;margin: 0 auto 200px;'>
        {content}
    </div>
</body>
</html>"""

def getHtmlContent(url, proxies=None):
    '''
    获取html
    '''
    if proxies is None:
        proxies = {"http": None, "https": None}
    res = requests.get(url, proxies)
    res.encoding = 'utf-8'
    return res.text


def reHtmlTags(cnt_html):
    '''
    替换图片src、元素、删除元素
    '''
    # 替换图片标签属性
    cnt_html = cnt_html.replace(
        "data-src", "src").replace('style="visibility: hidden;"', "")
    soup = BeautifulSoup(cnt_html, 'html.parser')
    # print(soup)
    # 删除评论和投票的html标签
    if soup.iframe:
        soup.iframe.decompose()
    # 用模板格式化
    comments = soup.findAll("img", {"class": "like_comment_pic"})
    styles = soup.find_all('style')
    content = soup.find('div', id='page-content')
    soup.find('div', id='js_tags').clear()
    soup.find('div', id='meta_content').clear()

    # 添加扩展的html片段
    extra_html = """
        <div style="width:100%;text-align:center;">
            <img style="width:200px;height:200px;" src="https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF" />
        </div>
    """
    extraSoup = BeautifulSoup(extra_html,"html.parser")
    content.append(extraSoup)

    imgs = soup.findAll('img', {'data-type':'png'})
    for img in imgs:
        old_src = img.get('src')
        time.sleep(1)
        new_src = upload_img(old_src)
        img['src'] = new_src
        # ratio = img['data-ratio']
        actual_width = img['data-w']
        if 'width' in img.attrs:
            actual_width = img['width']
        if '_width' in img.attrs:
            actual_width = img['_width']
        if 'data-s' in img.attrs:
            s = img['data-s']
            w = str(s).split(',')[0]
        else:
            w = 677
        w = '100%' if int(actual_width) > int(w) else str(actual_width) + 'px'
        # if w is not '100%': h = str(actual_width * ratio) + 'px'
        if 'width' not in img['style']: img['style'] = img['style'] + 'width: ' + w + ';'

    styles[0].string = styles[0].string + r'  img { width: 100%; }  '
    fmt_html = T_HTML.format(style=styles[0].string, content=content)
    html = fmt_html.replace(comments[0].attrs['src'], '') if comments else fmt_html
    html_name = getTimeStamp() + '.html'
    upload_html(html, html_name)
    time.sleep(1)
    save_json(soup, html_name)

def upload_html(html, html_name):
    print('上传文章html')
    if isTest:
        html_path = test_article_path + '/html/' + html_name
    else:
        html_path = article_path + '/html/' + html_name
    bucket.put_object(html_path, html)

def save_json(soup, html_name):
    # 获取 title description 保存到json文件
    meta_tag_image = soup.find('meta', {'property': 'og:image'})
    meta_tag_description = soup.find('meta', {'property': 'og:description'})
    meta_tag_author = soup.find('meta', {'property': 'og:article:author'})
    a_image = meta_tag_image['content']
    a_description = meta_tag_description['content']
    a_author = meta_tag_author['content']
    a_title = soup.find('h1', id='activity-name').text.strip()
    new_src = upload_img(a_image)
    time.sleep(1)
    # print(a_title, new_src, a_description)
    if isTest:
        json_path = test_article_path + '/config/config.json'
    else:
        json_path = article_path + '/config/config.json'
    if (bucket.object_exists(json_path)):
        json_content = bucket.get_object(json_path).read()
    else:
        json_content = '[]'
    data = json.loads(json_content)
    title_list = [d.get('title') for d in data]
    if a_title in title_list: 
        print('已经有标题相同的文章')
        return
    data_dict = {}
    data_dict['date'] = getShowDate()
    data_dict['title'] = a_title
    data_dict['image'] = new_src
    data_dict['author'] = a_author
    data_dict['description'] = a_description
    if isTest:
        data_dict['url'] = host + test_article_path + '/html/' + html_name
    else:
        data_dict['url'] = host + article_path + '/html/' + html_name
    print('预览文章链接 ' + data_dict.get('url'))
    data.insert(0, data_dict)
    out_content = json.dumps(data, ensure_ascii=False)
    bucket.put_object(json_path, out_content.encode())

def upload_img(src):
    response = requests.get(src)
    old_src_content = response.content
    img_name = getTimeStamp() + '.png'
    if isTest:
        img_path = test_article_path + '/img/' + getDate() + '/' + img_name
    else:
        img_path = article_path + '/img/' + getDate() + '/' + img_name
    bucket.put_object(img_path, old_src_content)
    print(f'上传图片成功 {host}{img_path}')
    return f'{host}{img_path}'

def remove_article(title):
    if isTest:
        json_path = test_article_path + '/config/config.json'
    else:
        json_path = article_path + '/config/config.json'
    if (bucket.object_exists(json_path)):
        json_content = bucket.get_object(json_path).read()
    else:
        json_content = '[]'
    data = json.loads(json_content)
    title_list = [d.get('title') for d in data]
    if title not in title_list: 
        print('没有找到要删除的文章')
        return
    data = [article for article in data if article.get('title') != title]
    out_content = json.dumps(data, ensure_ascii=False)
    bucket.put_object(json_path, out_content.encode())
    print(f'删除{title}成功')

def getTimeStamp ():
    return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

def getDate ():
    return str(datetime.datetime.now().strftime('%Y%m%d'))

def getShowDate ():
    return str(datetime.datetime.now().strftime('%Y-%m-%d'))

if __name__ == '__main__':
    questions = [
        inquirer.List('type', message="新增文章或者删除文章：", choices=['新增', '删除']),
        inquirer.List('test', message="是否测试", choices=['Yes', 'No']),
    ]
    answers = inquirer.prompt(questions)
    isTest = True if answers['test'] == 'Yes' else False
    if answers['type'] == '新增':
        url = input('公众号链接：')
        print('generate start')
        source = getHtmlContent(url)
        reHtmlTags(source)
    elif answers['type'] == '删除':
        title = input('输入要删除的文章的标题：')
        if title:
            print('remove')
            remove_article(title)
