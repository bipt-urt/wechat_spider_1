import urllib.request
import urllib.parse
import urllib
import http.cookiejar
import json


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
#print(list3)
response3=str(urllib.request.urlopen(list3).read())
if int(response3[14:17])==200:
	testresponse3=response3.split("\"")
	testresponse3=testresponse3[1]
	print('===============================成功登陆===============================')
#print(response3)
#print(testresponse3)

response3=urllib.request.urlopen(testresponse3 + '&fun=new').read().decode("utf-8", "replace")
ticket=response3.split(">")
ticket=ticket[12]
ticket=ticket.split("<")
ticket=ticket[0]
print('=========================开始获取您的各种信息=========================')
#print(ticket)
#找到ticket


Skey=response3.split(">")
Skey=Skey[6]
Skey=Skey.split("<")
Skey=Skey[0]
print('======================================================================')
#print(Skey)
#找到Skey


Uin=response3.split(">")
Uin=Uin[10]
Uin=Uin.split("<")
Uin=Uin[0]
print('=========================您即将交出的所有信息=========================')
#print(Uin)
#找到Uin


Sid=response3.split(">")
Sid=Sid[8]
Sid=Sid.split("<")
Sid=Sid[0]
print('==========================………………………………………………==========================')
#print(Sid)
#找到Sid


list4='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?skey='+Skey+'&r=-1493979626&lang=zh_CN&pass_ticket='+ticket
#print(list4)
postData={'BaseRequest':{"Uin":Uin,"Sid":Sid,"Skey":Skey,"DeviceID":"e899027140826785"}}
response4= urllib.request.urlopen(list4, json.dumps(postData).encode('utf-8')).read()
print('======================================================================')
with open("data.txt","wb") as f:
	f.write(response4)
with open("data.txt", "r", encoding="utf-8") as f:
	content=f.read()
	target=json.loads(content)
	#print(target.keys())
datalist=target['MemberList']
for data in datalist:
	print(data['PYQuanPin'], data['NickName'])

#获得用户好友信息


