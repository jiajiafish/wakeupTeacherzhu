import schedule
import time
from wxpy import *
from random import choice
bot=Bot()
data = bot.groups().search('数字新技术')[0]
def wakeup():

    list = [
        '朱旭老师睡觉了吗',
        '大佬已经休息了,只有我在看视频',
        '苹果双卡双待秀的飞起啊',
        '冒个泡证明不是大佬',
        '苹果今年发布了几款新品',
        '哎',
        '苹果也用参数化了',
    ]
    data.send(choice(list))
# def job():
#     print("I'm working...")
#
#
#
#
schedule.every(10).minutes.do(wakeup)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
#
while True:
    schedule.run_pending()
    time.sleep(1)