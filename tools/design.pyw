from threading import Thread
from multiprocessing import Process
import tkinter as tk
import tkinter.messagebox as messagebox
from myOwnPackage import ppi, ml
from PIL import Image, ImageTk
##import os
##from bs4 import BeautifulSoup

##from win32 import win32gui
##from win32 import win32con
##from win32 import win32api
##import re
##import sys
####import os
##
##from subprocess import run
##def callback():
##    messagebox.showwarning('错误','系统错误，请重试！')


##def virus(r):
##    root = tk.Tk()
##    root.title("草泥马")
##    root.geometry("500x600")
####    app = tk.Frame(root)
####    app.grid()
##    label = tk.Label(root,text='''
##     卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼卢本伟牛逼
##''', font = ('Arial', 18), width = 500, wraplength = 800)
##    label.place(x = 100, y = 50, anchor = "center")
##    root.mainloop()

##def virus():
##    run("mspaint",shell=True)

##def kaicmd(obj):
##    for i in range(0, 3):
##        t = Thread(target = virus)
##        t.start()
#######################################################
##def resize(w, h, w_box, h_box, pil_image):  
##  ''' 
##  resize a pil_image object so it will fit into 
##  a box of size w_box times h_box, but retain aspect ratio 
##  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例 
##  '''  
##  f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
##  f2 = 1.0*h_box/h  
##  factor = min([f1, f2])  
##  #print(f1, f2, factor) # test  
##  # use best down-sizing filter  
##  width = int(w*factor)  
##  height = int(h*factor)  
##  return pil_image.resize((width, height), Image.ANTIALIAS) 

########################################################    
def buil(e, order):
    t = Thread(target = ml.rn, args = (order,))
    t.start()

##def changeWp(e):
##    p = Process(target = bgiSelect, args = (e,))
##    p.start()

def ds():
    root = tk.Tk()
    root.title("电脑已经中病毒了")
    root.geometry("400x280")
##    app = tk.Frame(root)
##    app.grid()
    btn = tk.Button(root, text = "计算器")
    btn.place(x=30, y=30, anchor="center")
    btn.bind("<Button-1>",lambda event:buil(event,"calc"))
    btn2 = tk.Button(root, text = "画板")
    btn2.place(x=80, y=30, anchor="center")
    btn2.bind("<Button-1>", lambda event:buil(event,"mspaint"))
    btn3 = tk.Button(root, text = "记事本")
    btn3.place(x=131, y=30, anchor="center")
    btn3.bind("<Button-1>", lambda event:buil(event,"notepad"))
    btn4 = tk.Button(root, text = "桌面共享")
    btn4.place(x=190, y=30, anchor="center")
    btn4.bind("<Button-1>", lambda event:buil(event,"DeskTopShare"))
    btn5 = tk.Button(root, text = "飞秋")
    btn5.place(x=250, y=30, anchor="center")
    btn5.bind("<Button-1>", lambda event:buil(event,"C:/Users/Administrator/Desktop/v5_mole/FeiQ.exe"))
    btn6 = tk.Button(root, text = "谷歌")
    btn6.place(x=30, y=80, anchor="center")
    btn6.bind("<Button-1>", lambda event:buil(event,"chrome"))
    btn7 = tk.Button(root, text = "HBuilderX")
    btn7.place(x=95, y=80, anchor="center")
    btn7.bind("<Button-1>", lambda event:buil(event,"D:/HBuilderX/HBuilderX.exe"))
    btn8 = tk.Button(root, text = "虚拟机")
    btn8.place(x=171, y=80, anchor="center")
    btn8.bind("<Button-1>", lambda event:buil(event,"D:/Tesy/vmware.exe"))
    btn9 = tk.Button(root, text = "putty")
    btn9.place(x=230, y=80, anchor="center")
    btn9.bind("<Button-1>", lambda event:buil(event,"C:/Users/Administrator/Desktop/putty.exe"))
    btn10 = tk.Button(root, text = "控制台")
    btn10.place(x=290, y=80, anchor="center")
    btn10.bind("<Button-1>", lambda event:buil(event,"cmd"))
    btn11 = tk.Button(root, text = "迅雷")
    btn11.place(x=30, y=131, anchor="center")
    btn11.bind("<Button-1>", lambda event:buil(event,"D:/Thunder/Program/ThunderStart.exe -StartType:DesktopIcon"))
    btn12 = tk.Button(root, text = "百度云")
    btn12.place(x=80, y=131, anchor="center")
    btn12.bind("<Button-1>", lambda event:buil(event,"D:/BaiduNetdisk/BaiduNetdisk.exe"))
    btn13 = tk.Button(root, text = "火狐")
    btn13.place(x=131, y=131, anchor="center")
    btn13.bind("<Button-1>", lambda event:buil(event, "C:/Program Files/Mozilla Firefox/firefox.exe"))
    btn14 = tk.Button(root, text = "扫雷")
    btn14.place(x=180, y=131, anchor="center")
    btn14.bind("<Button-1>", lambda event:buil(event, "C:/Program Files/Microsoft Games/Minesweeper/MineSweeper.exe"))
    btn15 = tk.Button(root, text = "蜘蛛纸牌")
    btn15.place(x=240, y=131, anchor="center")
    btn15.bind("<Button-1>", lambda event:buil(event, "C:/Program Files/Microsoft Games/SpiderSolitaire/SpiderSolitaire.exe"))
    btn16 = tk.Button(root, text = "红心大战")
    btn16.place(x=50, y=180, anchor="center")
    btn16.bind("<Button-1>", lambda event:buil(event, "C:/Program Files/Microsoft Games/Hearts/Hearts.exe"))
    btn17 = tk.Button(root, text = "注册表")
    btn17.place(x=120, y=180, anchor="center")
    btn17.bind("<Button-1>", lambda event:buil(event, "regedit"))
    btn18 = tk.Button(root, text = "组策略")
    btn18.place(x=190, y=180, anchor="center")
    btn18.bind("<Button-1>", lambda event:buil(event, "gpedit"))
    btn19 = tk.Button(root, text = "更换壁纸")
    btn19.place(x=100, y=220, anchor="center")
    btn19.bind("<Button-1>", bgiSelect)
##  root.protocol("WM_DELETE_WINDOW", callback)
    root.mainloop()

#######################################################
allImages = []
for i in range(0, 12):
    allImages.append("C:/Users/Administrator/Desktop/v5_mole/wp/wallp" + str(i) + ".jpg")
allImagesForSelected = []
def ui(e, url):
    ml.setWallPaperBMP(url)

def change(obj):
    obj.bind("<Button-1>", lambda event: ui(event, allImages[allImagesForSelected.index(obj)]))    
def bgiSelect(e):
    rot = tk.Toplevel()
##    sb = tk.Scrollbar(root)
##    sb.pack(side = "right",fill = "y")
##    lb = tk.Listbox(root, yscrollcommand=sb.set)
##    lb.pack(side = "left",fill = "both")
##    sb.config(command=lb.yview)
##    canvas = tk.Canvas(rot,width=730, height=1870, scrollregion=(0,0,730,1870))
##    canvas.place(x = 10, y = 10) #放置canvas的位置
##    vbar = tk.Scrollbar(canvas,orient = "vertical",command = canvas.yview) #竖直滚动条
##    vbar.place(x = 700,width = 20, height = 770)
##    #vbar.configure(command = canvas.yview)
##    canvas.config(yscrollcommand = vbar.set) #设置  
    for i in allImages:
        load = Image.open(i)
        w, h = load.size
        pil_image_resized = ppi.resize(w, h, 300, 300, load)
        render= ImageTk.PhotoImage(pil_image_resized)
        img = tk.Label(rot, image=render, width="190", height="180")
        img.image = render
        num = allImages.index(i)
        if num >= 3:
            gao = (num - num%3)/3
            img.place(x = (num%3 * 220) + 20, y = gao * 202)
        else:
            img.place(x = (num * 220) + 20, y = 0)
        allImagesForSelected.append(img)
    for e in allImagesForSelected:
        change(e)
           
    rot.title("电脑已经中病毒了")
    rot.geometry("730x800+0+0")
    rot.resizable(width = False,height = True)
    rot.maxsize(710,912)
    rot.mainloop()
    
ds()














    
