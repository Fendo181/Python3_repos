#scores = [40,50,70,90] # list
#
#
## イテレータ
#print ("イテレータ文")
#it= iter(scores)
#
#print (next(it)) #40
#print (next(it)) #50
#print ("Hello Iterator")
#print (next(it)) 
#print (next(it))
#
#print ("for文")
## forの内部でもイテレータを使っている
#
#for score in scores:
#		print(score)

# リストでは実現できない無限の要素を持つイテレータを作る。

def get_infinite(): #ジェネレーター(イテレータを作る関数)
	i = 0
	while True:
			yield i*2 #次の要素を日っぱてくる
			i += 1

g = get_infinite()

print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))


