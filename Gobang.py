#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as messagebox

#���̽����
class ChessBoard(object):
    #��ʼ��һ��15*15��List��ȫ����'@'���
    def __init__(self):
        self.result = [['@' for i in range(15)] for j in range(15)]

    #���Ӻ�ı�List��Ӧ������ֵ���ɹ�����True��ʧ�ܷ���False��ʧ����Ϊ�ô��Ѿ�������
    def set(self,rowIndex,columnIndex,player):
        if self.result[rowIndex][columnIndex] == '@':
            self.result[rowIndex][columnIndex] = player
            return True
        else:
            return False

    #���ص�ǰλ���Ƿ��Ѿ������ӣ��з���True
    def get_isplaced(self,rowIndex,columnIndex):
        if self.result[rowIndex][columnIndex] == '@':
            return False
        else:
            return True

    #�ж���Ӯ��û�������'@'����Ӯ����'B',��Ӯ����'R'
    def CheckResult(self):
        rowData = []
        stringResult = ''
        for rows in self.result:
            stringResult += ''.join(rows)
            rowData.append(''.join(rows))
        columnData = [stringResult[i:225:15] for i in range(15)]
        #��б��'\'�Խ��ߣ����ȴ��ڵ���5�ĶԽ��߶���ͳ��
        BackSlashData = [stringResult[i:225-i*15:16] for i in range(11)] + [stringResult[i*15:225:16] for i in range(1,11)]
        #��б��'/'�Խ���
        SlashData = [stringResult[14+i*15:221:14] for i in range(11)] + [stringResult[i:60+(i-4)*15:14] for i in range(4,14)]
        for row in rowData+columnData+BackSlashData+SlashData:
            if 'BBBBB' in row:
                return 'B'
            elif 'RRRRR' in row:
                return 'R'
        return '@'
        
#������,���������������ߣ�������룬��ɫ
def checkered(canvas,width,height,interval,color = 'black'):
   # �����������
   for x in range(0,width,interval):
      canvas.create_line(x, 0, x, height, fill=color)
   # �����������
   for y in range(0,height,interval):
      canvas.create_line(0, y, width, y, fill=color)

#��Բ��������������x���꣬y���꣬�뾶������ɫ���߿���
def circle(canvas, x, y, r=13,color = 'black',width = 0):
    id = canvas.create_oval(x-r, y-r, x+r, y+r,fill=color,width = width)
    return id

#Restart��ť��Ӧ�¼�
def restart():
    #������̻������ػ�����
    global isBlack
    cav.delete('all')
    checkered(cav,length_board,length_board,length_interval)
    chessBoard.__init__()
    isBlack = True
    lab['text'] = 'Black Turn...'

#����
def dropDown(event):
    #�жϵ�ǰ���λ���Ƿ������ӣ���ֱ�ӷ���
    row_index = event.y//30
    column_index = event.x//30
    if (chessBoard.get_isplaced(row_index,column_index)):
        return
    #�õ�Ӧ�û�Բ�����꣬��Բ���ı�lab����ʾ
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
    #�ı����̽�����ֵ    
    if chessBoard.set(row_index,column_index,player):
        result = chessBoard.CheckResult()
        if(result == 'B'):
            messagebox.showinfo('WinInfo','Black Win!')
            restart()
        elif(result == 'R'):
            messagebox.showinfo('WinInfo','Red Win!')
            restart()
      
     
#��ʼ�����ڣ����֣������̵ȣ�
def initWindow(master,cav,lab):
    #���������
    master.title("Gobang")
    master.resizable(width=False, height=False) #���ɱ�, �߿ɱ�,Ĭ��ΪTrue
    #Label��ʾ���ӻغ���Ϣ
    #lab = tk.Label(master,text ='Black Turn')
    lab.grid(row = 0,column = 1)
    #����Canvas��������
    #cav = tk.Canvas(master,width = 451,height = 451,highlightthickness = 0)
    cav.grid(row = 1,column = 1)
    checkered(cav,length_board,length_board,length_interval)
    #������Canvas
    cav.grid(row = 1,column = 1)
    #�������߻������������ã��޹���
    cav_leftBlank = tk.Canvas(master,width = 5)
    cav_leftBlank.grid(row = 0,column = 0,rowspan=3)
    cav_rightBlank = tk.Canvas(master,width = 5)
    cav_rightBlank.grid(row = 0,column = 2,rowspan=3)
    #���¿�ʼ��ť
    btn = tk.Button(master,text = 'Restart',command = restart)
    btn.grid(row =2,column = 1)
    #circle(cav,15,15,13,'red')
        

#���̵ı߳�
length_board = 451
#���̼��
length_interval = 30
#���ӷ���TrueΪ�ڷ����ӻغϣ�FalseΪ�췽���ӻغ�
isBlack = True
master = tk.Tk()
cav = tk.Canvas(master,width = 451,height = 451,highlightthickness = 0)
lab = tk.Label(master,text ='Black Turn...')
chessBoard = ChessBoard()
initWindow(master,cav,lab)
#���������������а�
cav.bind("<Button-1>",dropDown)
tk.mainloop()