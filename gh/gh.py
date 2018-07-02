import urllib.request
import urllib.parse
import urllib
import http.cookiejar
header={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"utf-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Host":"h.highpin.cn",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://h.highpin.cn/ManageJob/PubNewJob",
    "Cookie":"pgv_pvi=7566289920; RK=PghhFkyxYh; ptcz=9bdcbf5e4f2ca72dce7cce6857944a6b238aaf287bce69e517c441d98e9ebc2a; wxuin=1460522711; webwxuvid=8a1a67e149b7bfc09941b0c58279bfc307c60ea19b714582a5b802554fe3b72c11d614d1a1625db0165644cf5e7d3283; mm_lang=zh_CN; ptui_loginuin=1144042303@qq.com; pt2gguin=o1144042303; ptisp=ctc; pgv_si=s3084923904; uin=o1144042303; skey=@JUaU83Qp3; wxpluginkey=1530508082; webwx_auth_ticket=CIsBEImalIkBGoABiA56gbtZ87UgF5y+9EvPjo7S3yp8GShVScT7Y3ArxUgBARBNFozQKj9N1bdocwMLkMUS3uyQgAosTJO0voplHISFzb7Yzvl+npxHReTnsG5lR8xjJDYHdoRUvDjKT/Qn2kQoZlumQKcrRIwOSWruLfTOYDOhjKg8ra/OQOuhotE=; wxloadtime=1530512357_expired",
    "Connection":"keep-alive"
    }
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r=opener.open("http://example.com/")
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
#获取二维码


list2='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid='+a+'&tip=1&r=-1226959975&_=1530235316523'
testresponse2=408
while testresponse2==408:
	response2=urllib.request.urlopen(list2).read()
	testresponse2=str(response2)
	testresponse2=testresponse2[14:17]
	testresponse2=int(testresponse2)
#没有扫码返回


list3='https://login.wx2.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid='+a+'&tip=0&r=-1241709442&_=1530250055109'
response3=str(urllib.request.urlopen(list3).read())
if int(response3[14:17])==200:
	testresponse3=response3.split("\"")
	testresponse3=testresponse3[1]
response3=urllib.request.urlopen(testresponse3+ '&fun=new').read().decode("utf-8", "replace")
response3=response3.split(">")
response3=response3[12]
response3=response3.split("<")
response3=response3[0]
#点击登录进入

list4='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1493979626&lang=zh_CN&pass_ticket='+response3
response4=urllib.request.urlopen(list4).read().decode('utf-8')
print(response4)
#获得用户好友信息

