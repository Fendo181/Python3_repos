from urllib.request import urlopen
#例外処理のライブラリ
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

#例外処理のライブラリ
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("This Server ccould not be found")
else:
    print("it Works!")
    bs4obj = BeautifulSoup(html.read(),"html.parser")
    print (bs4obj.body.h1)
