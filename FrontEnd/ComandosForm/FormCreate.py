import tkinter as tk
import tkinter.font as tkFont
#from Analizador.Comandos.esencial import Leer
class Create:
    def __init__(self, root):
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

        self.inputBody=tk.Entry(root)
        self.inputBody["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputBody["font"] = ft
        self.inputBody["fg"] = "#333333"
        self.inputBody["justify"] = "center"
        self.inputBody.place(x=170,y=200,width=337,height=30)

        self.inputName=tk.Entry(root)
        self.inputName["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputName["font"] = ft
        self.inputName["fg"] = "#333333"
        self.inputName["justify"] = "center"
        self.inputName.place(x=170,y=150,width=337,height=30)

        self.inputPath=tk.Entry(root)
        self.inputPath["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputPath["font"] = ft
        self.inputPath["fg"] = "#333333"
        self.inputPath["justify"] = "center"
        self.inputPath.place(x=170,y=250,width=338,height=30)

    def GButton_364_command(self):
        comando = []
        comando.append('create')
        subcomando = []
        subcomando.append(['-name->', self.inputName.get()])
        subcomando.append(['-path->', self.inputPath.get()])
        subcomando.append(['-body->', self.inputBody.get()])
        comando.append(subcomando)
        print(comando)
        #analizar = Leer()
        #analizar.comando(comando)

if __name__ == "__main__":
    root = tk.Tk()
    Create = Create(root)
    root.mainloop()
