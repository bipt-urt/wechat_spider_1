import urllib.request
import urllib.parse
import urllib.error
import urllib
import http.cookiejar
import json
import csv

def main():
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'),
		('Host', 'wx.qq.com'),
		('Accept', 'application/json, text/plain, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'),
		('Referer', 'https://wx.qq.com/'),
		('DNT', '1')]
	urllib.request.install_opener(opener)


code_html="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb"
code=urllib.request.urlopen(code_html).read().decode('utf-8')
#获取二维码的生成值
code1=code.find('\"')
str_code=code[code1+1:-2]
code_login='https://login.weixin.qq.com/qrcode/'
code_login=code_login+str_code
code=urllib.request.urlopen(code_login).read()
with open("qrcode.jpg","wb") as f:
	f.write(code)
print("=================已生成二维码，请扫码登录=================")
#根据test_html的值确认是否扫码，408-未扫码；201为已经扫码
test_html='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=' + str_code + '&tip=1&r=-1226830344&_=1530235185585'
test_login=408
while test_login==408:	
	test_login=str(urllib.request.urlopen(test_html).read())
	test_login=int(test_login[14:17])

#登陆成功后，值为200，并截取response中的网页
test_html='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid='+str_code+'&tip=0&r=-1238840899&_=1530247191641'
print("=================已扫码成功，请点击登录按钮=================")
login_html=str(urllib.request.urlopen(test_html).read())
if int(login_html[14:17])==200:
	login_confirm=login_html.find('\"')
	login_confirm=login_html[login_confirm+1:-2]

login_after=login_confirm+ '&fun=new'
cookies_number=(urllib.request.urlopen(login_after).read().decode("utf-8","replace"))
#print(cookies_number)
#截取pass-cookies码
pass_ticket=cookies_number.split(">")
pass_ticket=pass_ticket[12]
pass_ticket=pass_ticket.split("<")
pass_ticket=pass_ticket[0]

skey=cookies_number.split(">")
skey=skey[6]
skey=skey.split("<")
skey=skey[0]

uin=cookies_number.split(">")
uin=uin[10]
uin=uin.split("<")
uin=uin[0]

sid=cookies_number.split(">")
sid=sid[8]
sid=sid.split("<")
sid=sid[0]
#PI=pull-information
PI_html='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?skey='+skey+'&r=-1494086531&lang=zh_CN&pass_ticket='+pass_ticket
postData = {
		'BaseRequest': {
			'Uin': uin,
			'Sid': sid,
			'Skey': skey,
			"DeviceID":"e687649266955355"
		}
}
print("=================正在生成好友信息，请稍等.....=================")
response1= urllib.request.urlopen(PI_html, json.dumps(postData).encode('utf-8')).read()
with open('data.txt', 'wb') as f:
		f.write(response1)
with open("yjy.txt", "r", encoding="utf-8") as f:
		content=f.read()
		target=json.loads(content)
dataList=target['MemberList']
with open("data.csv","w",newline="") as datacsv:
	for element in dataList:
		for thing in element:
			element[thing]=str(element[thing])
		print(element['NickName'])
		datacsv.write("."+element['NickName']+","+element['RemarkName']+","+element['EncryChatRoomId']+","+element['ContactFlag']+","+element['Signature']+","+element['City']+","+element['Province']+","+element['VerifyFlag']+'\n')
print("=================已将信息录入data.csv中，请查看！=================")