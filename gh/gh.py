import urllib.request
import urllib.parse
url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb"
response=urllib.request.urlopen(url)
html=(response.read()).decode('utf-8')
html=html.split("\"")
a=html[1]
print(a)
b=str("https://login.weixin.qq.com/qrcode/")
c=b+a
print(c)
response=urllib.request.urlopen(c).read()
with open("qrcode.jpg", "wb") as f:
	f.write(response)