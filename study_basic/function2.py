# 関数 返り値が返ってくる。

def say_hi():
	# print("hi")
	return "hi"
#これ以降の処理は実行されないです。
	print("Hello")

# あくまでも値が返ってくるので、関数呼び出しでは標示されない
say_hi() 
msg = say_hi()

print (msg)

def test():
	# 関数の中身を今書かないであとで記述したい時にpassを入れる。
	pass

msg = test()
# 何も返ってこないので`None`が返ってくる。
print (msg)


