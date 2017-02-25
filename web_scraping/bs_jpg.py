from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

try:
    #先頭が(../img/gifts/img),末尾が(.jpg)のファイルを抽出してくる。
    images=bsObj.findAll("img",{"src":re.compile("\.\.\/img./gifts/img.*\.jpg")})
except AttributeError as e:
    print("なんらかのエラー")

for image in images:
    print(image["src"])


