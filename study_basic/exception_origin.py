# 独自の例外処理を作る


class MyException(Exception):
	# 空のクラスを作る
	pass

def div(a,b):
	try:
		if( b < 0):
			raise MyException("not minus!")
	#例外発生時の処理
	except ZeroDivisionError:
		print ("not by zaro")
	#例外発生時の処理
	except MyException as e:
		# eには先程自分で作った独自の例外処理のエラーメッセージが入っている
		print (e) 

	
	#例外が発生しなかった時の処理
	else:
		print("no exception!")
	#例外が発生しようが、しないようが最期に実行に実行して欲しい処理を記述する
	finally:
		print("-- end -- 処理が終わりました")
div(10,-3)
div(10,0)
