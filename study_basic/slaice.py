scores_lists= [40,50,60,70,100]
scores_tuples = (40,50,60,70,100)

print ("要素番号と中身")

for i,scores_list in enumerate(scores_lists):
		print ("{0}:{1}".format(i,scores_list))

print ("リスト{0}".format(scores_lists[1:4]))
print ("タプル{0}".format(scores_tuples[1:4]))


print ("終点のみ指定 [:2]")
print (scores_lists[:2])

print ("始点のみ指定 [3:]")
print (scores_lists[3:])

print ("末尾から要素数から-3まで  [-3:]")
print (scores_lists[-3:])

# 文字列でも使える。

s = "Hello"
print (s[1:4]) #ello
