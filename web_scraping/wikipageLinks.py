from urllib.request import urlopen
from bs4 import BeautifulSoup

req = urlopen("https://www.wikiwand.com/en/Aaron_Swartz")
bsObj = BeautifulSoup(req,"html.parser")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
