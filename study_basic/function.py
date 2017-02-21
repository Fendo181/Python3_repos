# 関数
# 
def say_hi(name,age):
	print ("Hi! {0} age({1})".format(name,age))

# 関数呼び出し
say_hi("tom",23)
say_hi("Bob",24)


# デファルト設定
def say_endo(name="endo",age=23):
	print ("Hi! {0} age({1})".format(name,age))

say_endo()
say_endo("steave")

# 順番は関係なく引数を与える。
say_endo(age=18,name="Takahashi")

