#一般的なlambda

# 2倍にして返す
myfunc = lambda x:x*2

print (myfunc(2))
print (myfunc(4))


#lambda とmap(list)を組み合わせて要素を5倍にする。
li = [1,2,3,4]
print(li)
#リスト型に変換する。
li2 = list(map(lambda n:n*5,li))
print (li2)
