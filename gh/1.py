def convert(_content):
	res = ""
	ignore = False
	for letter in _content:
		if ignore:
			if letter == ">":
				ignore = False
		else:
			if letter == "<":
				ignore = True
			else:
				res += letter
	return res

def main():
	with open("target.txt", "r", encoding="gb2312") as f:
		content = f.read()
		print(convert(content))

if __name__ == "__main__":
	main()