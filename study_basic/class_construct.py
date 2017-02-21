class User:
	count = 0
	#コンストラクタ(初期値)
	def __init__(self,name):
		# クラス変数
		User.count += 1;
		# インスタンス変数
		self.name = name

print(User.count)

tom = User("Tom")
bob = User("Bob")
print(User.count)

# クラスのプロパティであるから、tomのインスタからでも呼び出す事が出来る。
print("tom is count {0}".format(tom.count))

