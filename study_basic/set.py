a = set([5,4,8,5])

a = {5,4,8,5,8}
print (a)


#要素の中に5があるか確認する。
print (5 in a)

#要素を追加する。
a.add(2) #位置はバラバラである
print (a)

#要素を削除する。
a.remove(8)
print (a)

#要素の数を取得する。
print(len(a))

a1 = {1,3,5,8}
b1 = {3,5,4,9}

for i,a in enumerate(a1):
	print("a{0}:{1}".format(i,a))

for i,b in enumerate(b1):
	print("b{0}:{1}".format(i,b))


print("(|):和集合")
print (a1 | b1)
print("(&):積集合")
print (a1 & b1)
print ("(-):差集合")
print (a1 - b1)

