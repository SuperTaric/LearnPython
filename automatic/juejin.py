"""
掘金自动登录签到
"""
import os
import requests
import configparser
import time
import schedule
import dominate
from log import log
from emailFun import send_email
from dotenv import load_dotenv, find_dotenv
from dominate.tags import *

# 获取配置文件
config = configparser.ConfigParser()
config.read("./config.ini")
juejin_config = config["juejin"]
load_dotenv(find_dotenv('.env'))

uuid = juejin_config["uuid"]
aid = juejin_config["aid"]
_signature = os.environ.get('_SIGNATURE')
cookie = os.environ.get('COOKIE')

signUrl = f'https://api.juejin.cn/growth_api/v1/check_in?aid={aid}&uuid={uuid}&_signature={_signature}&spider=0'
raffleUrl = f'https://api.juejin.cn/growth_api/v1/lottery/draw?aid={aid}&uuid={uuid}&spider=0'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "cookie": cookie,
}

log(signUrl)
log(raffleUrl)

is_signIn_success = 0
signIn_error_msg = ''
is_raffle_success = 0
raffle_error_msg = ''

def signIn():
    result = requests.post(signUrl, headers = headers)
    data = result.json()
    if data.get('err_no') == 0:
        global is_signIn_success
        is_signIn_success = 1
    else:
        global signIn_error_msg
        is_signIn_success = 0
        signIn_error_msg = data.get('err_msg')
    log(data.get('err_msg'))

def raffle():
    result = requests.post(raffleUrl, headers = headers)
    data = result.json()
    if data.get('err_no') == 0:
        global is_raffle_success
        is_raffle_success = 1
    else:
        global raffle_error_msg
        is_raffle_success = 0
        raffle_error_msg = data.get('err_msg')
    log(data.get('err_msg'))
    return data.get('data')

def run():
    signIn()
    time.sleep(1)
    data = raffle()
    time.sleep(1)
    sender = os.environ.get('MAIL_USER')
    receivers = [os.environ.get('MAIL_USER')]
    if is_raffle_success == 1:
        lottery_name = data.get('lottery_name')
        lottery_image = data.get('lottery_image')
        total_lucky_value = data.get('total_lucky_value')
        sing_text = f"签到{ is_signIn_success and '成功' or '失败:' + signIn_error_msg }"
        d = div()
        i = img(src=lottery_image)
        h = ul()
        with h:
            li(sing_text)
            li("抽奖成功")
            li("幸运值：" + str(total_lucky_value))
            li("中奖名称：" + lottery_name)
        d.add(h)
        d.add(i)
        print(d)
        send_email(sender, receivers, '掘金签到抽奖', str(d))
    else:
        h = ul()
        sing_text = f"签到{ is_signIn_success and '成功' or '失败:' + signIn_error_msg }"
        raffle_text = f"抽奖失败: {raffle_error_msg}"
        d = div()
        with h:
            li(sing_text)
            li(raffle_text)
        d.add(h)
        print(d)
        send_email(sender, receivers, '掘金签到抽奖', str(d))

def job():
    log('job start')
    run()

# schedule.every().day.at("09:00").do(job)
schedule.every(10).seconds.do(job)

if __name__ == "__main__":
    log('juejin.py start')
    while True:
        schedule.run_pending()
        time.sleep(1)