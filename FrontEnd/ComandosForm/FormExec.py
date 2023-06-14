import tkinter as tk
import tkinter.font as tkFont
from Analizador.Comandos.esencial import Leer
from Analizador.gramar import gramarMain
from Analizador.cripto import decrypt_string
class Exec:
    def __init__(self, root,Leer):
        #setting title
        root.title("undefined")
        self.miaTexto=''
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
        comando = []
        comando.append('exec')
        subcomando = []
        subcomando.append(['-path->', self.inputpath.get()])
        comando.append(subcomando)
        #print(comando)
        self.miaTexto=self.analizar.comando(comando)#retorna el txt
        arrayText = self.miaTexto.split('\n')#connfigure..../demas
        resultado = gramarMain("txt", arrayText[0])
        self.analizar.comando(resultado)
        if self.analizar.comando.llave!="":#desencriptar 
            decrypt_string(bytes(self.analizar.comando.llave,
                           'utf-8'), bytearray.fromhex(arrayText[1]))
        else:#encriptado
            resultado = gramarMain("txt", self.miaTexto)
            self.analizar.comando(resultado)

# if __name__ == "__main__":
#     root = tk.Tk()
#     Exec = Exec(root)
#     root.mainloop()
