# 例外処理

def div(a,b):
	try:
		#0除算
		print (a/b)
	#例外発生時の処理
	except ZeroDivisionError:
		print ("not by zaro")
	#例外が発生しなかった時の処理
	else:
		print("no exception!")
	#例外が発生しようが、しないようが最期に実行に実行して欲しい処理を記述する
	finally:
		print("-- end -- 処理が終わりました")
div(10,3)
div(10,0)
