from urllib.request import urlopen
html = urlopen("https://www.2ch.net/")
print (html.read())
