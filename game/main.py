import tkinter
from tkinter import *
from tkinter import ttk 
import os
import time
from tkinter import messagebox
from tkinter import PhotoImage

root = Tk()
root.title("Game")
root.geometry("540x540")

X = "X"
O = "O"

class Play:
    def sprint(self):
        for i in range(3): 
            print(self.playtable[i * 3:(i + 1) * 3]) 
            
    def __init__(self):
        self.image1 = PhotoImage(file="C:/Users/rulko/Desktop/крестики/sex.png")
        self.image2 = PhotoImage(file="C:/Users/rulko/Desktop/крестики/fuck.png")
        self.currentplayer = 2
        self.playtable = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def check(self):
        if self.playtable[0] == self.playtable[1] == self.playtable[2] != 0:
            return self.playtable[0]
        if self.playtable[3] == self.playtable[4] == self.playtable[5] != 0:
            return self.playtable[3]
        if self.playtable[6] == self.playtable[7] == self.playtable[8] != 0:
            return self.playtable[6]

        if self.playtable[0] == self.playtable[3] == self.playtable[6] != 0:
            return self.playtable[0]
        if self.playtable[1] == self.playtable[4] == self.playtable[7] != 0:
            return self.playtable[1]
        if self.playtable[2] == self.playtable[5] == self.playtable[8] != 0:
            return self.playtable[2]

        if self.playtable[0] == self.playtable[4] == self.playtable[8] != 0:
            return self.playtable[0]
        if self.playtable[2] == self.playtable[4] == self.playtable[6] != 0:
            return self.playtable[2]
        
        return 3

    def click(self, but_name):
        if self.currentplayer % 2 == 0:   
            
            but_name.config(state="disabled", image = self.image1)
            self.currentplayer += 1
        else:
            
            but_name.config(state="disabled", image = self.image2)
            self.currentplayer += 1
        
        if but_name == btn[0]:
            self.playtable[0] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[1]:
            self.playtable[1] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[2]:
            self.playtable[2] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[3]:
            self.playtable[3] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[4]:
            self.playtable[4] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[5]:
            self.playtable[5] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[6]:
            self.playtable[6] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[7]:
            self.playtable[7] = 1 if self.currentplayer % 2 == 0 else 2
        if but_name == btn[8]:
            self.playtable[8] = 1 if self.currentplayer % 2 == 0 else 2
       
        winner = self.check()
        if winner != 0 :
            if winner == 1:  
                print("ИГРОК О ВЫИГРАЛ")
                messagebox.showinfo("Победа", "ИГРОК О ВЫИГРАЛ")  
                root.destroy()
            if winner == 2:  
                print("ИГРОК Х ВЫИГРАЛ")
                messagebox.showinfo("Победа", "ИГРОК Х ВЫИГРАЛ") 
                root.destroy()
                      
fuck = Play()

btn = []
for i in range(9):
    btn.append("b"+str(i+1))
for i in btn:
    i = Button(text=" ", state="normal", command=lambda btn=i: fuck.click(btn), width=5, height=3)
    for c in range(3):
        for r in range(3):
            i.grid(row=c, column=r, sticky="nsew")



for i in range(1, 4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

