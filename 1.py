#first-code
from bs4 import BeautifulSoup
import requests
f1=open("links.txt","wt")
w=requests.get("https://varzesh3.com")
soup=BeautifulSoup(w.content)
divs=soup.find_all("div","news-main-list")
for div in divs:
    links=div.find_all("a")
    for link in links:
        if "news" in link["href"]:
            print(link["href"],"\n")
            f1.write(link["href"]+"\n")
f1.close()