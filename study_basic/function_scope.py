# 関数

msg = "Hello Global!" #グローバル変数

#def say_hi():
#	#関数の中で宣言された変数はこの関数の中でのみ有効である。
#	#スコープ
#	msg = "Hello Local!" # ローカル変数
#	print (msg)

def say_hi():
	#中からは書き換えできない
	global msg 
	msg = "change global 2 local"
	print (msg)#グローバル変数を参照できる。


say_hi()
print (msg)
