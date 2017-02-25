from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

try:
    #2つの属性をもつ要素をLambda式で記述する。
    tag=bsObj.findAll(lambda tag: len(tag.attrs)==2)
except AttributeError as e:
    print("なんらかのエラー")

print(tag)


