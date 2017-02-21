# アクセス制限


class User:
	count = 0
	#コンストラクタ
	def __init__(self,name):
		User.count += 1;
	# クラス外からアクセスしない様に明示的に宣言する。
		self.__name = name
	#インスタンスメソッド(インデントは上に合わせる!)
	def say_hi(self):
		print("hi! {0}".format(self.__name))


tom = User("Tom")
bob = User("Bob")

## アクセスできないと見える
#print (tom.__name)

## 実はこれでアクセスできてしまいます!
print (tom._User__name)
