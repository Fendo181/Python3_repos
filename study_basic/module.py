# モジュール
# この時はモジュール名を指定してあげないといけない。
#import user

# モジュールから指定した関数やクラスを読み込む
# この時はモジュール名を指定しなくて良い。
from user import AdminUser,User




#class User:
#	def __init__(self,name):
#		self.name = name
#	def say_hi(self):
#		print("Hi!{0}".format(self.name))
#
#class AdminUser(User):
#	def __init__(self,name,age):
#		#self.name = name
#		super().__init__(name)
#	def say_hello(self):
#		print("Hello!{0}".format(self.name))

#from 
#tom =user.User("tom")
tom =User("tom")

# from 
bob = AdminUser("bob",23);



print (bob.name)
bob.say_hi()#親クラスのメソッド
bob.say_hello() #抽象クラスのメソッド



