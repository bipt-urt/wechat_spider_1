from wxpy import *
bot = Bot()
my_friend = bot.friends().search('这是一个低调高冷的名字')[0]
my_friend.send_image('qrcode.jpg')