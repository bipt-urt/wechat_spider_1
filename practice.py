import json
with open("yjy.txt", "r", encoding="utf-8") as f:
	#for line in f:
		#print(":)" + line)
	content=f.read()
	target=json.loads(content)
	#print(target)
	print(target)
	#print(len(target["MemberList"]))