from aip import AipSpeech

APP_ID = '11465615'
API_KEY = 'WmRigeU1kTF502pV6zWcl74K'
SECRET_KEY = 'eh3EaAhUuTruAGn8MuUDguVGOsjBW7gg'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('大家好，我们是专业实习第二小组。组长是又笨蛋又智障的王万霖同学，\
我们的组员有帅气的郭汉、美丽的杨金瑶、聪明的刘仁可、稳重的梁永宁和性感的曾海涛同学。\
我们的口号是：好好写程序争取快速跑路', 'zh', 3, {
    'vol': 5, 'per':3, 'spd':4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)