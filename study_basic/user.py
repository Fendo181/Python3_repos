# User モジュール

class User:
	def __init__(self,name):
		self.name = name
	def say_hi(self):
		print("Hi!{0}".format(self.name))

class AdminUser(User):
	def __init__(self,name,age):
		#self.name = name
		super().__init__(name)
	def say_hello(self):
		print("Hello!{0}".format(self.name))

print ("モジュールから出力したHello!です")
