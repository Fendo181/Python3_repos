#map

#3倍にする関数

def triple(n):
	return n*4

#map(関数,イテレータ)を使う
#mapはジェネレーターを返すので、そのままprintできない。
#今回はlistで固める。
print (list(map(triple,[1,2,3])))

# lambda

# わざわざ関数も作るのも面倒だ。

#lammmbda 引数:処理

print (list(map(lambda n:n*5,[1,2,3])))
