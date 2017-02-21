# filter(関数,イテレータ)

#偶数だけ抽出する。

def is_even(n):
	return n % 2 == 0

print (list(filter(is_even,range(20))))

print (list(filter(lambda n: n%2 == 0,range(20))))



