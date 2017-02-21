name = "Endo"
score = 52.6

# %で文字列埋め込み(整数は%d)
print("name: %s,score:%f" %(name,score))

# 桁数表示幅を指定する。
# %10s =10の幅を持たせる。%10.2f=10の幅を持たせて小数点2桁にする。
print("name: %10s,score:%10.2f" %(name,score))
# 左揃えにする。
print("name: %-10s,score:%-10.2f" %(name,score))


# {}を使う。文字列formatを気にしなくて良い
print("name:{0},score:{1}".format(name,score))
# 桁数を指定する。
print("name:{0:10s},score:{1:10.2f}".format(name,score))
# >右揃え <左揃え
print("name:{0:>10s},score:{1:<10.2f}".format(name,score))

