import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import PhotoImage

root = tk.Tk()
root.title("Game")
root.geometry("540x540")

class Play:
    def __init__(self):
        self.playTable = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.massiveButt = []
        self.currentplayer = 2
        self.image1 = PhotoImage(file="C:/Users/rulko/Desktop/крестики/newfuck.png")
        self.image2 = PhotoImage(file="C:/Users/rulko/Desktop/крестики/newsex.png")
        self.create_buttons()

    def create_buttons(self):
        for r in range(3):        
            for c in range(3):
                index = r * 3 + c
                newBut = tk.Button(text=" ", command=lambda idx=index: self.pressBut(idx))
                
                newBut.grid(row=r, column=c, sticky=tk.NSEW)
                self.massiveButt.append(newBut)
        
        
        for i in range(3):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def pressBut(self, index):
        print("pressed", index) 
        if self.currentplayer % 2 == 0:
            self.massiveButt[index].config(image=self.image1, state="disabled")
            self.playTable[index] = 2
        else:
            self.massiveButt[index].config(image=self.image2, state="disabled")
            
            self.playTable[index] = 1
        self.currentplayer += 1
        anal = self.checkwinner()
        if anal != 0:
            if anal == 1:
                messagebox.showinfo("WON", "PLAYER O WON")
                root.destroy()
            if anal == 2:
                messagebox.showinfo("WON", "PLAYER X WON")
                root.destroy()
            if anal == 44:
                messagebox.showinfo("WON", "draw")
                root.destroy()

    def checkwinner(self):
        for i in range(3):
            if self.playTable[i * 3] == self.playTable[i * 3 + 1] == self.playTable[i * 3 + 2] != 0:
                return self.playTable[i * 3]

        for i in range(3):
            if self.playTable[i] == self.playTable[i + 3] == self.playTable[i + 6] != 0:
                return self.playTable[i]

        if self.playTable[0] == self.playTable[4] == self.playTable[8] != 0:
            return self.playTable[0]
        if self.playTable[2] == self.playTable[4] == self.playTable[6] != 0:
            return self.playTable[2]
        count = 0
        for i in self.playTable:
            if i != 0:
                count+=1
        if count > 8:
            return 44
        return 0

sex = Play() 
root.mainloop()