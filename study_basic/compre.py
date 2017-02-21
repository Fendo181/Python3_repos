#内包表記(Comprehensions)

#G 0-9までのリストを作る。
# range(10) で 0 から 9 のリストができるので、そのリストから 1 つずつ要素を取り出してこちらの i に入れて、それをそのまま i として取り出す、という意味になります。

print (range(10))
print (list(range(10)))

print ([i for i in range(10) ])

#それぞれの要素を3倍にする。
# forの内部構造も結局の所イテレータを使っているのでこの様に要素を取り出して加工する事が出来る。
print ([i*3 for i in range(10) ])
#これをmapで書くとこうなる。
print (list(map(lambda n:n*3,range(10))))

# 内包表記でfilterの様に使う。

#3倍した値から偶数を取り出す。
print ([ i*3 for i in range(10) if i % 2 == 0])

#これをfilter()で書くとこうなる。
#list3 = list(map(lambda n:n*3,range(10)))
#print (list(filter(lambda n: n%2 == 0, list(map(lambda n:n*3,range(10))))))

# ジェネレーター ()
print (i*3 for i in range(10) if i % 2 == 0) #<generator object <genexpr> at 0x7f021d05ae60>

#ジェネレーター式をこういう風に使う。
compre_gen = (i*3 for i in range(10) if i % 2 == 0) 

for i in compre_gen:
		print(i)
# 集合型
print ({i*3 for i in range(10) if i % 2 == 0  })

