from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageurl):
    global pages
    html = urlopen("https://www.wikiwand.com/en/Aaron_Swartz")
    bsObj = BeautifulSoup(html,"html.parser")
    #例外処理
    try:
        print(bsObj.h1.get_text())
        #print(bsObj.find(id="content").findAll("p"[0]))
        #print(bsObj.find(id="ca-edit").find("span").find(a).attrs['href'])
    except AttributeError:
        print("This page is missing something! No woories though")

    for link in bsObj.findAll("a",href=re.compile("(http)")):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    #新しいページに出会った
                    newPage=link.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    #再帰
                    getLinks(newPage)

#実行
getLinks("")
