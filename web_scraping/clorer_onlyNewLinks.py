from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageurl):
    global pages
    html = urlopen("https://www.wikiwand.com/en/Aaron_Swartz")
    bsObj = BeautifulSoup(html,"html.parser")
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
