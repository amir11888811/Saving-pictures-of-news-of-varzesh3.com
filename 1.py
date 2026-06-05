from bs4 import BeautifulSoup
import requests
f1=open("links.txt","wt",encoding="utf-8")
r=requests.get("https://www.varzesh3.com")
soup=BeautifulSoup(r.text, "html.parser")
links=set()
for a in soup.find_all("a",href=True):
    href=a["href"]
    if "/news/" in href:
        if href.startswith("/"):
            href = "https://www.varzesh3.com"+href
        if href not in links:
            links.add(href)
            f1.write(href + "\n")
f1.close()