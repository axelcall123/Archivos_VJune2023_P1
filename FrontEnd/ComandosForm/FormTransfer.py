import tkinter as tk
import tkinter.font as tkFont
#from Analizador.Comandos.esencial import Leer
class Transfer:
    def __init__(self, root,Leer):
        #setting title
        root.title("undefined")
        #setting window size
        self.analizar = Leer
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
        GLabel_559["text"] = "Transfer"
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
        GLabel_819["text"] = "From"
        GLabel_819.place(x=70,y=150,width=70,height=25)

        GLabel_824=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_824["font"] = ft
        GLabel_824["fg"] = "#333333"
        GLabel_824["justify"] = "center"
        GLabel_824["text"] = "To"
        GLabel_824.place(x=30,y=190,width=141,height=46)

        self.inputFrom=tk.Entry(root)
        self.inputFrom["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputFrom["font"] = ft
        self.inputFrom["fg"] = "#333333"
        self.inputFrom["justify"] = "center"
        self.inputFrom.place(x=170,y=150,width=337,height=30)

        self.inputTo=tk.Entry(root)
        self.inputTo["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputTo["font"] = ft
        self.inputTo["fg"] = "#333333"
        self.inputTo["justify"] = "center"
        self.inputTo.place(x=170,y=200,width=338,height=30)

        GLabel_126=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_126["font"] = ft
        GLabel_126["fg"] = "#333333"
        GLabel_126["justify"] = "center"
        GLabel_126["text"] = "Mode"
        GLabel_126.place(x=60,y=250,width=81,height=34)

        self.inputMode=tk.Entry(root)
        self.inputMode["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputMode["font"] = ft
        self.inputMode["fg"] = "#333333"
        self.inputMode["justify"] = "center"
        self.inputMode.place(x=170,y=250,width=327,height=30)

    def GButton_364_command(self):
        comando = []
        comando.append('transfer')
        subcomando = []
        subcomando.append(['-from->', self.inputFrom.get()])
        subcomando.append(['-to->', self.inputTo.get()])
        subcomando.append(['-mode->', self.inputMode.get()])
        comando.append(subcomando)
        print(comando)
        #analizar = Leer()
        #analizar.comando(comando)
# if __name__ == "__main__":
#     root = tk.Tk()
#     Transfer = Transfer(root)
#     root.mainloop()
