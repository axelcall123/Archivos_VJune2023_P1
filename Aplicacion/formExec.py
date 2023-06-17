import tkinter as tk
import tkinter.font as tkFont


from Aplicacion.Analizador.gramar import grammarInput
from tkinter import messagebox as MessageBox
from Aplicacion.Analizador.Comandos.esencial import Leer


class Exec:
    def __init__(self, root,analizar):
        self.analizar=analizar
        #setting title
        root.title("Exec")
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
        GLabel_559["text"] = "Exec"
        GLabel_559.place(x=180,y=20,width=279,height=45)

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
        GLabel_819["text"] = "Path"
        GLabel_819.place(x=70,y=150,width=70,height=25)

        self.inputpath=tk.Entry(root)
        self.inputpath["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputpath["font"] = ft
        self.inputpath["fg"] = "#333333"
        self.inputpath["justify"] = "center"
        self.inputpath.place(x=160,y=150,width=321,height=31)

    def GButton_364_command(self):
        print(self.inputpath.get())
        if((self.inputpath.get()!="")):  
            #no se ingreso name(opcional)
                stringInput="exec "+ "-path->"+self.inputpath.get()
                grammarInput(stringInput,self.analizar)
        else:
            MessageBox.showerror("Error!", "Llena todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    Exec = Exec(root)
    root.mainloop()
