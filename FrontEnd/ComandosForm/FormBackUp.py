import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

class BackUp:
    def __init__(self, root):
        self.comboGetmode=""

        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_559=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_559["font"] = ft
        GLabel_559["fg"] = "#333333"
        GLabel_559["justify"] = "center"
        GLabel_559["text"] = "Back up"
        GLabel_559.place(x=170,y=20,width=279,height=45)

        GButton_364=tk.Button(root)
        GButton_364["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_364["font"] = ft
        GButton_364["fg"] = "#ffffff"
        GButton_364["justify"] = "center"
        GButton_364["text"] = "Ejec. Comando"
        GButton_364.place(x=250,y=400,width=115,height=41)
        GButton_364["command"] = self.GButton_364_command

        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "Mode"
        GLabel_819.place(x=70,y=150,width=70,height=25)

        def comboModeFunction(event):
            self.comboGetmode=comboBoxmode.get()
        comboBoxmode=ttk.Combobox(root,values=["Cloud","Local"])
        ft = tkFont.Font(family='Times',size=10)
        comboBoxmode.set("Selecciona un modo")
        comboBoxmode.bind('<<ComboboxSelected>>',comboModeFunction)
        comboBoxmode.place(x=170,y=150,width=337,height=30)

    def GButton_364_command(self):
        print(self.comboGetmode)

if __name__ == "__main__":
    root = tk.Tk()
    app = BackUp(root)
    root.mainloop()
