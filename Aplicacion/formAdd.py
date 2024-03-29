import tkinter as tk
import tkinter.font as tkFont


from Aplicacion.Analizador.gramar import grammarInput
from Aplicacion.Analizador.Comandos.esencial import Leer
from tkinter import messagebox as MessageBox
class Add:
    def __init__(self, root,analizar):
        self.analizar=analizar
        #setting title
        root.title("Add")
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
        GLabel_559["text"] = "Add"
        GLabel_559.place(x=170,y=20,width=279,height=45)

        bttnEjecComando=tk.Button(root)
        bttnEjecComando["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnEjecComando["font"] = ft
        bttnEjecComando["fg"] = "#ffffff"
        bttnEjecComando["justify"] = "center"
        bttnEjecComando["text"] = "Ejec. Comando"
        bttnEjecComando.place(x=250,y=400,width=115,height=41)
        bttnEjecComando["command"] = self.bttnEjecComando_command

        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "Path"
        GLabel_819.place(x=70,y=150,width=70,height=25)

        GLabel_824=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_824["font"] = ft
        GLabel_824["fg"] = "#333333"
        GLabel_824["justify"] = "center"
        GLabel_824["text"] = "Body"
        GLabel_824.place(x=30,y=220,width=141,height=46)

        self.inputPath=tk.Entry(root)
        self.inputPath["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputPath["font"] = ft
        self.inputPath["fg"] = "#333333"
        self.inputPath["justify"] = "center"
        self.inputPath.place(x=170,y=150,width=337,height=30)

        self.inputBody=tk.Entry(root)
        self.inputBody["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputBody["font"] = ft
        self.inputBody["fg"] = "#333333"
        self.inputBody["justify"] = "center"
        self.inputBody.place(x=170,y=230,width=338,height=30)


    def bttnEjecComando_command(self):

        if((self.inputPath.get()!="")&(self.inputBody.get()!="")):   
                #Creando string
                stringInput="add "+ "-path->"+self.inputPath.get()+ " -body->"+self.inputBody.get()+""
                resultado=grammarInput(stringInput,self.analizar)
        else:
            MessageBox.showerror("Error!", "Llena todos los campos")

        


