"""
掘金自动登录签到
"""
import requests
import configparser
import time
from datetime import datetime

# 获取配置文件
config = configparser.ConfigParser()
config.read("./config.ini")
juejin_config = config["juejin"]

"""
由于特殊符号的问题暂不放入config文件中 
https://juejin.cn/user/center/signin?avatar_menu 页面
check_in_rules 接口可以拿到 _signature, uuid, aid
随便找一个包含 cookie 的接口就能拿到 cookie
可以拿到
"""
_signature = ''
cookie = ''
uuid = juejin_config["uuid"]
aid = juejin_config["aid"]

signUrl = f'https://api.juejin.cn/growth_api/v1/check_in?aid={aid}&uuid={uuid}&_signature={_signature}&spider=0'
raffleUrl = f'https://api.juejin.cn/growth_api/v1/lottery/draw?aid={aid}&uuid={uuid}&spider=0'

print(signUrl)
print(raffleUrl)
print(cookie)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "cookie": cookie,
}

def signIn():
    result = requests.post(signUrl, headers = headers)
    log(result.text)

def raffle():
    result = requests.post(raffleUrl, headers = headers)
    log(result.text)

def run():
    signIn()
    time.sleep(1)
    raffle()

def log(text):
    print(text)
    with open('./log.txt', mode='a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + text + '\n')

if __name__ == "__main__":
    run()