from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")

# greenだけ
#nameList = bsObj.findAll("span",{"class":"green"})
# redとgreen全て
nameList = bsObj.findAll("span",{"class":{"red":"green"}})
princeCount =bsObj.findAll(text="the prince")
#idとclassを指定する。
#titletagList = bsObj.findAll(id="title",class_="text")
for name in nameList:
    print(name.get_text())

print(len(princeCount))
