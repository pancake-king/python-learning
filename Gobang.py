#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as messagebox

#棋盘结果类
class ChessBoard(object):
    #初始化一个15*15的List，全部用'@'填充
    def __init__(self):
        self.result = [['@' for i in range(15)] for j in range(15)]

    #下子后改变List对应索引的值，成功返回True，失败返回False，失败因为该处已经有棋子
    def set(self,rowIndex,columnIndex,player):
        if self.result[rowIndex][columnIndex] == '@':
            self.result[rowIndex][columnIndex] = player
            return True
        else:
            return False

    #返回当前位置是否已经有棋子，有返回True
    def get_isplaced(self,rowIndex,columnIndex):
        if self.result[rowIndex][columnIndex] == '@':
            return False
        else:
            return True

    #判断输赢，没结果返回'@'，黑赢返回'B',红赢返回'R'
    def CheckResult(self):
        rowData = []
        stringResult = ''
        for rows in self.result:
            stringResult += ''.join(rows)
            rowData.append(''.join(rows))
        columnData = [stringResult[i:225:15] for i in range(15)]
        #反斜线'\'对角线，长度大于等于5的对角线都得统计
        BackSlashData = [stringResult[i:225-i*15:16] for i in range(11)] + [stringResult[i*15:225:16] for i in range(1,11)]
        #正斜线'/'对角线
        SlashData = [stringResult[14+i*15:221:14] for i in range(11)] + [stringResult[i:60+(i-4)*15:14] for i in range(4,14)]
        for row in rowData+columnData+BackSlashData+SlashData:
            if 'BBBBB' in row:
                return 'B'
            elif 'RRRRR' in row:
                return 'R'
        return '@'
        
#画棋盘,参数：画布，宽，高，间隔距离，颜色
def checkered(canvas,width,height,interval,color = 'black'):
   # 按间隔画竖线
   for x in range(0,width,interval):
      canvas.create_line(x, 0, x, height, fill=color)
   # 按间隔画横线
   for y in range(0,height,interval):
      canvas.create_line(0, y, width, y, fill=color)

#画圆，参数：画布，x坐标，y坐标，半径，充填色，边框宽度
def circle(canvas, x, y, r=13,color = 'black',width = 0):
    id = canvas.create_oval(x-r, y-r, x+r, y+r,fill=color,width = width)
    return id

#Restart按钮响应事件
def restart():
    #清除棋盘画布并重画棋盘
    global isBlack
    cav.delete('all')
    checkered(cav,length_board,length_board,length_interval)
    chessBoard.__init__()
    isBlack = True
    lab['text'] = 'Black Turn...'

#下子
def dropDown(event):
    #判断当前点击位置是否有棋子，有直接返回
    row_index = event.y//30
    column_index = event.x//30
    if (chessBoard.get_isplaced(row_index,column_index)):
        return
    #得到应该画圆的坐标，画圆并改变lab的显示
    global isBlack    
    x_draw = (event.x//30)*30 + 15
    y_draw = (event.y//30)*30 + 15
    color = 'red'
    text = 'Black Turn...'
    player = 'R'    
    if  isBlack:
        color = 'black'
        text = 'Red Trun...'
        player = 'B'
        isBlack = False
    else:
        isBlack = True
    circle(cav,x_draw,y_draw,13,color)
    lab['text'] = text
    #改变棋盘结果类的值    
    if chessBoard.set(row_index,column_index,player):
        result = chessBoard.CheckResult()
        if(result == 'B'):
            messagebox.showinfo('WinInfo','Black Win!')
            restart()
        elif(result == 'R'):
            messagebox.showinfo('WinInfo','Red Win!')
            restart()
      
     
#初始化窗口（布局，画棋盘等）
def initWindow(master,cav,lab):
    #主窗口相关
    master.title("Gobang")
    master.resizable(width=False, height=False) #宽不可变, 高可变,默认为True
    #Label显示下子回合信息
    #lab = tk.Label(master,text ='Black Turn')
    lab.grid(row = 0,column = 1)
    #棋盘Canvas，画棋盘
    #cav = tk.Canvas(master,width = 451,height = 451,highlightthickness = 0)
    cav.grid(row = 1,column = 1)
    checkered(cav,length_board,length_board,length_interval)
    #画棋子Canvas
    cav.grid(row = 1,column = 1)
    #左右两边画布，美观作用，无功能
    cav_leftBlank = tk.Canvas(master,width = 5)
    cav_leftBlank.grid(row = 0,column = 0,rowspan=3)
    cav_rightBlank = tk.Canvas(master,width = 5)
    cav_rightBlank.grid(row = 0,column = 2,rowspan=3)
    #重新开始按钮
    btn = tk.Button(master,text = 'Restart',command = restart)
    btn.grid(row =2,column = 1)
    #circle(cav,15,15,13,'red')
        

#棋盘的边长
length_board = 451
#棋盘间隔
length_interval = 30
#下子方，True为黑方下子回合，False为红方下子回合
isBlack = True
master = tk.Tk()
cav = tk.Canvas(master,width = 451,height = 451,highlightthickness = 0)
lab = tk.Label(master,text ='Black Turn...')
chessBoard = ChessBoard()
initWindow(master,cav,lab)
#画布与鼠标左键进行绑定
cav.bind("<Button-1>",dropDown)
tk.mainloop()