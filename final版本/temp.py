import tkinter
import random
import threading
import time
from randomdraw import *
from txt_solve import *
from PIL import Image, ImageTk
from tkinter import ttk
from makeimg import *


#初始化窗口
root=tkinter.Tk()
root.title("随机名单")
root.geometry('1300x800')
root.resizable(False,False)
root.flag = True
root.start=False
k='22'
#背景

canvas = tkinter.Canvas(root,
    width = 1300,      # 指定Canvas组件的宽度
    height = 800,      # 指定Canvas组件的高度
    bg = 'white')  #背景颜色
backim = Image.open("ii.png")
im = ImageTk.PhotoImage(backim)
canvas.create_image(650,400,image = im)

canvas.pack()

#关键词 时间范围

label1 = tkinter.Label(root, text="输入关键词：",bg='#920a0c',fg='#FFFFFF',font = ("宋体", 20,"normal"))
label1.place(x=768, y=503)
label2 = tkinter.Label(root, text="请选择时间范围：",bg='#920a0c',fg='#FFFFFF',font = ("宋体", 20,"normal"))
label2.place(x=768, y=542)
labelmonth1 = tkinter.Label(root, text="月",bg='#920a0c',fg='#FFFFFF',font = ("宋体", 20,"normal"))
labelmonth1.place(x=820, y=581)
labelday1 = tkinter.Label(root, text="日-",bg='#920a0c',fg='#FFFFFF',font = ("宋体", 20,"normal"))
labelday1.place(x=915, y=581)
labelmonth2 = tkinter.Label(root, text="月",bg='#920a0c',fg='#FFFFFF',font = ("宋体", 20,"normal"))
labelmonth2.place(x=1025, y=581)
labelday2 = tkinter.Label(root, text="日",bg='#920a0c',fg='#FFFFFF',font = ("宋体", 20,"normal"))
labelday2.place(x=1113, y=581)

#中奖名单
first = tkinter.Label(root,text='',bg='#920a0c',font = ("宋体", 25,"normal"),fg='#F4D267')
first.place(x=819,y=209,width=166,height=41)

second = tkinter.Label(root,text='',bg='#920a0c',font = ("宋体", 25,"normal"),fg='#F4D267')
second.place(x=819,y=250,width=166,height=41)

third = tkinter.Label(root,text='',bg='#920a0c',font = ("宋体", 25,"normal"),fg='#F4D267')
third.place(x=819,y=291,width=166,height=41)

four = tkinter.Label(root,text='',bg='#920a0c',font = ("宋体", 25,"normal"),fg='#F4D267')
four.place(x=819,y=332,width=166,height=41)

five = tkinter.Label(root,text='',bg='#920a0c',font = ("宋体", 25,"normal"),fg='#F4D267')
five.place(x=819,y=373,width=166,height=41)

six = tkinter.Label(root,text='',bg='#920a0c',font = ("宋体", 25,"normal"),fg='#F4D267')
six.place(x=819,y=414,width=166,height=41)

#滚动
def switch():
    root.flag=True
    win=[]
    print(k)
    win=draw_winner(k)
    print(win)
    while root.flag:
        a=random.sample(win,6)
        first['text']=a[0]
        second['text']=a[1]
        third['text']=a[2]
        four['text']=a[3]
        five['text']=a[4]
        six['text']=a[5]
        time.sleep(0.03)


#开始按钮
def butStartClick():
   
    if(root.start==False):
       # win=draw_winner()
        #print(k)
        btnStart['text']='停！'
        t=threading.Thread(target=switch)
        t.start()
        root.start=True
    else:
        
        root.flag=False
        btnStart['text']='生成活跃度图'
        main()
        root.start=False
        
        #main()
        btnStart['text']='抽奖'
btnStart=tkinter.Button(root,text='抽奖',bg='#F4D267',font = ("华文彩云", 36,"normal"),fg='#920A0C',command=butStartClick)
btnStart.place(x=763, y=620, width=377, height=82)
#文本框
'''
name = tkinter.StringVar()
typeEntered = ttk.Entry(root, width=30, textvariable=name)
typeEntered.place(x=920, y=505, height=30)
typeEntered.focus() 
''' # 当程序运行时,光标默认会出现在该文本框中
def rtnkey(event=None):
    #print(e.get())
    global k
    k=e.get()
    #return e.get()

e = tkinter.StringVar()
entry = ttk.Entry(root, validate='key', textvariable=e, width=30)
entry.place(x=920, y=505, height=30)
entry.focus()  # 当程序运行时,光标默认会出现在该文本框中
entry.bind('<Return>', rtnkey)

#下拉框
numbermonth1 = tkinter.StringVar()
monthChosen1 = ttk.Combobox(root, width=3, textvariable=numbermonth1, font=("宋体", 15,"normal"))
monthChosen1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)     # 设置下拉列表的值
monthChosen1.place(x=770, y=581, height=30)      # 设置其在界面中出现的位置  column代表列   row 代表行
monthChosen1.current(0)

numberday1 = tkinter.StringVar()
monthChosen1 = ttk.Combobox(root, width=3, textvariable=numberday1, font=("宋体", 15,"normal"))
monthChosen1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)     # 设置下拉列表的值
monthChosen1.place(x=860, y=581, height=30)      # 设置其在界面中出现的位置  column代表列   row 代表行
monthChosen1.current(0)

numbermonth2 = tkinter.StringVar()
monthChosen2 = ttk.Combobox(root, width=3, textvariable=numbermonth2, font=("宋体", 15,"normal"))
monthChosen2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)     # 设置下拉列表的值
monthChosen2.place(x=970, y=581, height=30)      # 设置其在界面中出现的位置  column代表列   row 代表行
monthChosen2.current(0)

numberday2 = tkinter.StringVar()
monthChosen2 = ttk.Combobox(root, width=3, textvariable=numberday2, font=("宋体", 15,"normal"))
monthChosen2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)     # 设置下拉列表的值
monthChosen2.place(x=1060, y=581, height=30)      # 设置其在界面中出现的位置  column代表列   row 代表行
monthChosen2.current(0)

#启动主程序
root.mainloop()
