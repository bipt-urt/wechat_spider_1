import urllib.request
import urllib.parse
import urllib
import http.cookiejar
import json
import csv
import io
import sys
import random
from wxpy import *

print('start')


def main():
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0')]
	urllib.request.install_opener(opener)
# 然后正常使用urllib.urlopen().read()等即可，不需要使用任何特殊方法

if __name__ == "__main__":
	main()
#cookie


list1="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb"
response1=urllib.request.urlopen(list1)
html=(response1.read()).decode('utf-8')
html=html.split("\"")
a=html[1]
b=str("https://login.weixin.qq.com/qrcode/")
c=b+a
response1=urllib.request.urlopen(c).read()
with open("qrcode.jpg", "wb") as f:
	f.write(response1)
print('==============================生成二维码==============================')
#获取二维码


list2='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid='+a+'&tip=1&r=-1226959975&_=1530235316523'
testresponse2=408
while testresponse2==408:
	print('==============================请快点扫码==============================')
	response2=urllib.request.urlopen(list2).read()
	testresponse2=str(response2)
	testresponse2=testresponse2[14:17]
	testresponse2=int(testresponse2)
#没有扫码返回


list3='https://login.wx2.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid='+a+'&tip=0&r=-1241709442&_=1530250055109'
print('==============================赶紧点登陆==============================')
#print(list3)
response3=str(urllib.request.urlopen(list3).read())
if int(response3[14:17])==200:
	testresponse3=response3.split("\"")
	testresponse3=testresponse3[1]
	print('===============================成功登陆===============================')
#print(response3)
#print(testresponse3)

response3=urllib.request.urlopen(testresponse3 + '&fun=new').read().decode("utf-8", "replace")
#print(response3)
ticket=response3.split("</pass_ticket>")
ticket=ticket[0]
ticket=ticket.split("<pass_ticket>")
ticket=ticket[1]
print('=========================开始获取您的各种信息=========================')
print('=========================您即将交出的所有信息=========================')
#print(ticket)
#找到ticket


Skey=response3.split("</skey>")
Skey=Skey[0]
Skey=Skey.split("<skey>")
Skey=Skey[1]
print('======================================================================')
#print(Skey)
#找到Skey


Uin=response3.split("</wxuin>")
Uin=Uin[0]
Uin=Uin.split("<wxuin>")
Uin=Uin[1]
#print(Uin)
#找到Uin


Sid=response3.split("</wxsid>")
Sid=Sid[0]
Sid=Sid.split("<wxsid>")
Sid=Sid[1]
print('==========================………………………………………………==========================')
#print(Sid)
#找到Sid


list4='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?skey='+Skey+'&r=-1493979626&lang=zh_CN&pass_ticket='+ticket
#print(list4)
postData1={'BaseRequest':{"Uin":Uin,
						"Sid":Sid,
						"Skey":Skey,
						"DeviceID":"e899027140826785"}}
response4= urllib.request.urlopen(list4, json.dumps(postData1).encode('utf-8')).read()
print('======================================================================')


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
with open("data.txt","wb") as f:
	f.write(response4)
with open("data.txt", "r", encoding="utf-8") as f:
	content=f.read()
	target=json.loads(content)
	#print(target.keys())
datalist=target['MemberList']
#print(content)
#print(type(datalist))
#print(datalist)
with open("data.csv","w",encoding="gb18030",newline="") as datacsv:
	for data1 in datalist:
		for data2 in data1:
			data1[data2]=str(data1[data2]).replace('\n',"")
		#print(data1['NickName'])
		datacsv.write(data1['UserName']+','+data1['NickName']+','+data1['RemarkName']+','+data1['Signature']+','+data1['Province']+','+data1['SnsFlag']+"\n")
print('=========================您已经交出的所有信息=========================')
#获得用户好友信息


message=input('输入消息：')
result={}
for element in datalist:
	if element["RemarkName"]==Name:
		result=element
		break
	if element["NickName"]==Name:
		result=element
		break
choose=result['UserName']
#print(choose)
#print(type(choose))
#输入发送对象和发送信息


result2={}
list5='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1671848414'
postData2={"BaseRequest":{"Uin":Uin,
						"Sid":Sid,
						"Skey":Skey,
						"DeviceID":"e742471654104946"}}
response5= urllib.request.urlopen(list5, json.dumps(postData2).encode('utf-8')).read()
with open("mine.txt","wb") as f:
	f.write(response5)
with open("mine.txt", "r", encoding="utf-8") as f:
	content=f.read()
	target=json.loads(content)
result2=target['User']
#print(result2)
mine=result2['UserName']
#print(mine)


id=random.random()
id=str(id)[2:] + '1'

list6='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket='+ticket
postData3={'BaseRequest':
						{"Uin":Uin,
						"Sid":Sid,
						"Skey":Skey,
						"DeviceID":"e910132017991627"},
				"Msg":{"Type":1,
					"Content":message,
					"FromUserName":mine,
					"ToUserName":choose,
					"LocalID":id,
					"ClientMsgId":id},
					"Scene":0}
send_data=json.dumps(postData3,ensure_ascii=False)#转成能发中文
send_bytes=bytes(send_data,'utf-8').replace(b' ',b'')
html_send=urllib.request.Request(list6,send_bytes)
response6=urllib.request.urlopen(html_send)

#urllib.request.urlopen(list6, bytes(json.dumps(postData).encode('utf-8'))).read()

list7 = []
with open('data.csv','r', encoding="gb18030") as f:
	for line in f:
		row = []
		if line.find("@@") == -1:
			continue
		line = line.split(",")
		for element in line:
			row.append(element)
		list7.append(row)
#print(list7)


with open("group.csv","w",encoding="gb18030",newline="") as groupcsv:
	for i in list7:
		response7=i
		response7=str(response7)
		print(response7)
		groupcsv.write(response7+'\n')
#将群组写入csv