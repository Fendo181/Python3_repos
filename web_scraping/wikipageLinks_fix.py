from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

req = urlopen("https://www.wikiwand.com/en/Aaron_Swartz")
bsObj = BeautifulSoup(req,"html.parser")
for link in bsObj.find("ul",{"id":"main_menu"}).findAll("a",href=re.compile("^(/wiki/)")):
    if 'href' in link.attrs:
        print(link['href'])
