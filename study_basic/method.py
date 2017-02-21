# クラス
# メソッド(関数)


class User:
	count = 0
	#コンストラクタ
	def __init__(self,name):
		User.count += 1;
		self.name = name
	#インスタンスメソッド(インデントは上に合わせる!)
	def say_hi(self):
		print("hi! {0}".format(self.name))
	#クラスメソッド
	@classmethod#(デコレーター)
	def show_info(cls):
		print("{0}:instances".format(cls.count))


tom = User("Tom")
bob = User("Bob")

# インスタンスメソッド
#tom.say_hi()
#bob.say_hi()

# クラスメソッド
User.show_info()
User.show_info()



