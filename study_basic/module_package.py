# パッケージ = パッケージはフォルダがモジュール化されたもの


#(1) 一般的なモジュール呼び出し
#import mypackage.user 

#(2) を使って明示的に名前をつける。
#import mypackage.user as MyModule

#(3)fromで特定の関数のみ読み込む => パッケー名.モジュール名は省略して良い。
from mypackage.user import AdminUser


# (1) 
#tom =mypackage.user.User("tom")
#bob = mypackage.user.AdminUser("bob",23)
#
#print (tom.name)
#tom.say_hi()
#print (bob.name)
#bob.say_hello()

#(2)
#tom =MyModule.User("tom")
#bob = MyModule.AdminUser("bob",23)
#print (tom.name)
#tom.say_hi()
#print (bob.name)
#bob.say_hello()


#(3)
bob = AdminUser("bob",23)
print (bob.name)
bob.say_hi()
bob.say_hello()


#from 
#tom =user.User("tom")
#bob = AdminUser("bob",23)

#print (bob.name)
#bob.say_hi()#親クラスのメソッド
#bob.say_hello() #抽象クラスのメソッド



