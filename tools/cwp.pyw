import tkinter
from myOwnPackage import ml
import time
import requests
from threading import Thread
import re
import os


def get_photourl(photo_url):
    kw = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    try:
        r = requests.get(photo_url,headers = kw)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return 'wrong'

def get_url(url):
    kw = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    try:
        r = requests.get(url,headers = kw)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return 'wrong!!!!!!!!!!!'



def changeWallpaper():
    if not os.path.exists("D:/pa"):
        os.mkdir("D:/pa")
    result = get_url("https://wallhaven.cc/")
    items = re.findall(r'https://wallhaven.cc/w/.*?[a-zA-Z0-9]{6}', result.text, re.M)
    for item in items:
        time.sleep(3)
        aaa = item[23:]
        bbb = aaa[0:2]
        photourl = "https://w.wallhaven.cc/full/" + bbb + "/" + "wallhaven-" + aaa + ".jpg"
        result2 = get_photourl(photourl)
        ufo = "https://w.wallhaven.cc/full/" + bbb + "/" + "wallhaven-" + aaa + ".png"
        result3 = get_photourl(ufo)
        if result2 == "wrong":
            ufo = "https://w.wallhaven.cc/full/" + bbb + "/" + "wallhaven-" + aaa + ".png"
            result3 = get_photourl(ufo)
            with open("D:/pa/wpp.png", "wb") as f:
                f.write(result3.content)
                ml.setWallPaperBMP("D:/pa/wpp.png")
        else:
            with open("D:/pa/wp.jpg", "wb") as f:
                f.write(result2.content)
                ml.setWallPaperBMP("D:/pa/wp.jpg")
        
for i in range(0, 5):
    changeWallpaper()
##https://wallhaven.cc/w/zmm7mw
##https://w.wallhaven.cc/full/zm/wallhaven-zmm7mw.png
