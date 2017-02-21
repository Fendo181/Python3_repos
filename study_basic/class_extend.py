# クラスの継承

# User(親クラス) -> AdminUser(サブクラス)
class User:
	def __init__(self,name):
		self.name= name
		print ("親クラスでのnameは{0}".format(self.name))
	def say_hi(self):
		print("[親クラスのメソッド]Hi! {0}".format(self.name))

# クラスの継承
class AdminUser(User):
	def __init__(self,name,age):
		#nameは親クラスのコンストラクタを使う。
		# 親クラスはSuperで表現できる。
		#実質これがUser.nameって事かな?
		"""
		親クラス(Userの)__init__ メソッド
		(コンストラクタ=インスタンスメソッド)で
	 	name を初期化する処理がすでに存在するので、
		 それをサブクラス(AdminUser)の中でも再利用しよう、
		する為にsuper()を使うというものです。
		"""

		#初期化
		super().__init__(name)
	
		#これを呼び出す事で`self.nmae`が使える。
		self.age = age
		print ("子クラスでsuper()を使った親クラスのプロパティ呼び出すされるnameは{0}".format(self.name))
		
		# 
		#親クラスのプロパティを書き換える。
		self.name = "Endo"
		print ("子クラスで親クラスのプロパティを書き換えた後に呼び出されるnameは{}".format(self.name))

	def say_hello(self):
		print("Hello!! {0} age:{1}".format(self.name, self.age))
	#親クラスのメソッドのオーバーライド
	def say_hi(self):
		print ("[子クラス()でオーバーライド後のメソッド] hi {0}".format(self.name))

print("継承前の世界")
bob = User("Bob")
bob.say_hi()

print("継承後の世界")
bob = AdminUser("bob",22)
bob.say_hi()

print (bob.name)
# 小クラス(サブクラス)のインスタンスメソッド
bob.say_hello()
#親クラスのメソッドをOverrideする
bob.say_hi()
