# for文

# for 変数 in データの集合
# 処理

# range(0,10)なので、0から9が含まれる集合が作られる。
for i in range(0,10):
	if i == 5:
		#break
		# iが5の時にスキップする。
		continue
	print(i)
#終了後の処理
else:
	print("Finish!")
