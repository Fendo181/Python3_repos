# 辞書型 {"文字列":200,"文字列"}

sales = {"taguch":200,"fkoji":400}
print (sales["taguch"])

## 置き換え
#sales["taguch"] = 400
#print(sales["taguch"])
#
## 追加
#sales["dotinstall"] = 400
#print(sales)
#
##消去
#del(sales["fkoji"])
#print(sales)


# items()でkeyとitemを取得する。
for key,value in sales.items():
		print("{0}:{1}".format(key,value))
