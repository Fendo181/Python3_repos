from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.time)

#ページで見つかった全ての内部リンクをリストを取り出す。

def getInternalLinks(bsObj,includeUrl):
    includeUrl=urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    # "/"で始まる全てのリンクを見つける。
    for link in bsObj.findAll("a",href=re.compile("^(\/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])


#ページで見つかった全ての外部リンクをリストを取り出す。
def getExternalLinks(bsObj,excludeUrl):
    excludeUrl=urlparse(excludeUrl).scheme+"://"+urlparse(excludeUrl).netloc
    externalLinks = []
    # "http"か'www'で始まる全てのリンクを見つける。
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,"html.parser")
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("外部リンクはありません。")
        domain = (urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bsObj,startingPage)
        #再帰呼出し。
        #return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
        return getRandomExternalLink(internalLinks[random.randint(0,1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(staratingSite):
    externalLink = getRandomExternalLink(staratingSite)
    print("Random external link is :" + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://www.wikiwand.com/en/Aaron_Swartz")
