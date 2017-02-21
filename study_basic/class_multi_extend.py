# クラスの継承を考える。

# A,B->C

class A:
	def say_a(self):
		print("A")
	def say_hi(self):
		print("Hi Form A")

class B:
	def say_b(self):
		print("B")
	def say_hi(self):
		print("Hi Form B")

# クラスの多重継承

class C(A, B):
	pass

c = C()
c.say_a()
c.say_b()

c.say_hi() # Hi from Aになる。
