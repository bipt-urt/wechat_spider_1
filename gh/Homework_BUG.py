from wxpy import *
from pyecharts import Pie
import os
import xlwt

if __name__ == '__main__':
    bot = Bot(cache_path=True) #自动弹出QR.png二维码图片,开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
    bot.enable_puid() #puid 是 wxpy 特有的聊天对象/用户ID
    friendname = input(u'请输入你要聊天的人员名称：')

    friend=bot.friends().search(nick_name=friendname)[0]
    msg=input(u'请输入你要和他说的话：')
    friend.send(msg)

    yorn=input(u'你是否希望打印出所有微信好友的信息？（y/n）')
    for f in bot.friends():
        if f.sex==1:
            sex='男'
        elif f.sex==2:
            sex='女'
        print(f.name,sex,f.city,f.signature,f.remark_name)

    rows=len(bot.friends())
    # 新建一个excel文件
    file = xlwt.Workbook()
    # 新建一个sheet
    table = file.add_sheet('info', cell_overwrite_ok=True)

    # 写入数据table.write(行,列,value)
    table.write(0, 0, '姓名')
    table.write(0, 1, '备注')
    table.write(0, 2, '是否为朋友')
    table.write(0, 3,'城市')
    table.write(0, 4, '性别')
    table.write(0, 5, '省份')
    table.write(0, 6, '签名')

    i=1
    sex=''
    for f in bot.friends():
        #print(f.name,f.remark_name,f.is_friend,f.city,f.sex,f.province,f.signature)

        table.write(i, 0, f.name)
        table.write(i, 1, f.remark_name)
        table.write(i, 2, str(f.is_friend))
        table.write(i, 3, f.city)
        if f.sex==1:
            
            
        elif f.sex==2:
            sex='女'
        table.write(i, 4, sex)
        table.write(i, 5, f.province)
        table.write(i, 6, f.signature)

        i=i+1

    # 保存文件
    file.save('filex.xls')

    yn = input(u'你是否查看一下微信好友男女比例呢？（y/n）')
    if  yn=='y':
        male = female = other = 0
        friends = bot.friends()
        for i in friends[:]:
            sex = i.sex
            if sex == 1:
                male += 1
            elif sex == 2:
                female += 1
            else:
                other += 1
        total = len(friends)  # 计算总数
        print('您共有'+str(total)+'位好友！')

        #没有对人数相等进行判断
        if female>male :
            titlex='看来我还是喜欢女人多一些，不信看饼图'
        else:
            titlex='看来我还是喜欢男人多一些，不信看饼图'
        # 下面为分析
        attr = ["男性", "女性", "其他"]
        v1 = [float(male), float(female), float(other)]
        print(male,female,other)
        pie = Pie(titlex, title_pos='center')
        #pie.add("", attr, v1, radius=[60, 75], label_text_color=None, is_label_show=True,legend_orient='vertical', legend_pos='left')
        pie.add("性别统计", attr, v1, radius=[60, 75],legend_orient='vertical', legend_pos='left')
        #http://pyecharts.org/#/zh-cn/charts
        pie.render("sex.html")
        os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe" file:///'+os.getcwd()+'/sex.html')