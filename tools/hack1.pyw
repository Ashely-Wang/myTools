from arptool import Arp
import tkinter as tk
import tkinter.messagebox as messagebox
from threading import Thread
validIp = []
validtime = []
for i in range(0, 30):
    validtime.append(str(i))
for i in range(0, 255):
    validIp.append(str(i))
def test(e):
    data1 = sstr1.get().lstrip()
    data2 = sstr2.get().lstrip()
    if data1 in validIp and data2 in validtime:
        ipad = '192.168.0.' + data1
        t = Thread(target = Arp, args = (ipad, data2))
        t.start()
        messagebox.showwarning("成功", "目标主机将在" + data2 + "分钟后解除限制")
    else:
        if data1 not in validIp and data2 in validtime:
            messagebox.showwarning("警告", "主机范围是1-254，别瞎鸡巴乱输入！！")
        if data1 in validIp and data2 not in validtime:
            messagebox.showwarning("警告", "时间最大值为60分钟，别瞎鸡巴乱输入！！")
        if data1 not in validIp and data2 not in validtime:
            messagebox.showwarning("警告", "主机范围是1-254，别瞎鸡巴乱输入！！")




        
rot = tk.Tk()
lab1 = tk.Label(rot, text = "输入目标主机")
lab2 = tk.Label(rot, text = "输入限制时间(分钟)")
lab1.place(x = 50, y = 70)
lab2.place(x = 50, y = 120)
sstr1 = tk.StringVar()
sstr2 = tk.StringVar()
xls = tk.Entry(rot, textvariable=sstr1)
xls2 = tk.Entry(rot, textvariable=sstr2)
sstr1.set(" ")
sstr2.set(" ")
xls.place(x = 180, y = 70)
xls2.place(x = 180, y = 120)
btn = tk.Button(rot, text = '奥利给！！干他！', )
btn.place(x = 100, y = 180, anchor="center")
btn.bind("<Button-1>", test)


rot.geometry("450x260")
rot.mainloop()



##Arp('10.1.1.1', '5')






















