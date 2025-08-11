#second-code
from bs4 import BeautifulSoup
import requests
f1=open("links.txt","rt")
links=f1.read().splitlines()
f2=open("pictures.txt","wt")
for link in links:
    w=requests.get(link)
    soup=BeautifulSoup(w.content)
    pics= soup.find_all("img")
    for pic in pics:
        src = pic.get("src")
        if "pictures" in src and not "farakav" in src:
            f2.write(src+"\n")
            print(src)
f1.close()
f2.close()