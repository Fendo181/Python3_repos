# 配列っぽい?
scores = [40,50]

print (scores[0])
print (scores[1])


# 要素の個数を調べる = len
print ("要素の長さは:{0}".format(len(scores)))
# 要素の末尾にに追加する。 = append
scores.append(100) 
print (scores)
print ("要素の長さは:{0}".format(len(scores)))


print ("バリューだけ表示する。")

#  forと組み合わせる。
for score in scores:
		#各要素を順々に出力する。
		print(score)



# 何番目の要素かも取り出したい場合には、enumerate という命令を使えば OK です。

print ("要素数とバリューを表示する。")

for i,score in enumerate(scores):
		print ("{0}:{1}".format(i,score))
