#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from  tkinter.filedialog import askdirectory
import requests
import bs4

def selectPath():
    path_ = askdirectory()
    path_main.set(path_)

def start():
    url = url_main.get()
    path = path_main.get()
    a = 2


master = tk.Tk()
path_main = tk.StringVar()
url_main = tk.StringVar()
lab1 = tk.Label(master,text = '下载网址：').grid(row =0,column = 0)
entry1 = tk.Entry(master,textvariable = url_main).grid(row = 0,column = 1)
lab2 = tk.Label(master,text = '保存路径：').grid(row = 1,column = 0)
entry2 = tk.Entry(master,textvariable = path_main).grid(row = 1,column =1)
btn = tk.Button(master,text = '...',command = selectPath).grid(row = 1,column = 2)
btn_start = tk.Button(master,text = '下载',command = start).grid(row = 2,column = 1)
tk.mainloop()

