import requests
from bs4 import BeautifulSoup
import urllib.request
import os

url = 'http://pic.netbian.com/4kfengjing/'
a = requests.get(url)
print(a.status_code)
soup = BeautifulSoup(a.content,"html.parser")
images = soup.find_all("img")
i = 1
for image in images:
    image_src = image["src"]
    print(image_src)
    os.remove("pic.jpg")
    urllib.request.urlretrieve('http://pic.netbian.com/'+image_src,str("pic"))
    os.rename("pic","pic.jpg")
    stop = input("input:")
    if(stop=="TRUE"):
        break
    elif(stop=="FALSE"):
        urllib.request.urlretrieve('http://pic.netbian.com/'+image_src,str("pic"+str(i)))
        os.rename("pic"+str(i),"pic"+str(i)+".jpg")
    i+=1