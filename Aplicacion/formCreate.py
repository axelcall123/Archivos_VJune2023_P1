import tkinter as tk
import tkinter.font as tkFont

from Aplicacion.Analizador.gramar import grammarInput
from tkinter import messagebox as MessageBox
from Aplicacion.Analizador.Comandos.esencial import Leer

class Create:
    def __init__(self, root,analizar):
        self.analizar=analizar
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
        GLabel_559["text"] = "Create"
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
        GLabel_819["text"] = "Name"
        GLabel_819.place(x=70,y=150,width=70,height=25)

        GLabel_577=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_577["font"] = ft
        GLabel_577["fg"] = "#333333"
        GLabel_577["justify"] = "center"
        GLabel_577["text"] = "Body"
        GLabel_577.place(x=40,y=190,width=127,height=37)

        GLabel_824=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_824["font"] = ft
        GLabel_824["fg"] = "#333333"
        GLabel_824["justify"] = "center"
        GLabel_824["text"] = "Path"
        GLabel_824.place(x=30,y=240,width=141,height=46)

        self.body=tk.Entry(root)
        self.body["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.body["font"] = ft
        self.body["fg"] = "#333333"
        self.body["justify"] = "center"
        self.body.place(x=170,y=200,width=337,height=30)

        self.name=tk.Entry(root)
        self.name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.name["font"] = ft
        self.name["fg"] = "#333333"
        self.name["justify"] = "center"
        self.name.place(x=170,y=150,width=337,height=30)

        self.inputPath=tk.Entry(root)
        self.inputPath["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputPath["font"] = ft
        self.inputPath["fg"] = "#333333"
        self.inputPath["justify"] = "center"
        self.inputPath.place(x=170,y=250,width=338,height=30)

    def GButton_364_command(self):
        #print(self.body.get())
        #print(self.name.get())
        #print(self.inputPath.get())
        if((self.body.get()!="")&(self.name.get()!="")&(self.inputPath.get()!="")):  
            stringInput="create "+ "-name->"+self.name.get()+" -path->"+self.inputPath.get()+" -body->" +self.body.get()
            print(stringInput)
            grammarInput(stringInput,self.analizar)
        else:
            MessageBox.showerror("Error!", "Llena todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    Create = Create(root)
    root.mainloop()
