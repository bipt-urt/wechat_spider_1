import json

with open("yjy.txt", "r", encoding="utf-8") as f:
	content = f.read()
	target = json.loads(content)
print(len(target["MemberList"]))
print(target["MemberCount"])