import urllib.request
import urllib
url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb"
response=urllib.request.urlopen(url)
#输出回应的网址，并转化为字符串类型
html=(response.read()).decode('utf-8')
code1=html.find('\"')
str_code=html[code1+1:-2]
html1='https://login.weixin.qq.com/qrcode/'
html2=html1+str_code
response=urllib.request.urlopen(html2).read()
#print(response.read())
with open("qrcode.jpg","wb") as f:
	f.write(response)

