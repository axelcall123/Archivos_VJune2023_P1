import tkinter as tk
import tkinter.font as tkFont
from Aplicacion.formConfigure import Configure
from Aplicacion.formAdd import Add
from Aplicacion.formBackUp import BackUp
from Aplicacion.formCopy import Copy
from Aplicacion.formCreate import Create
from Aplicacion.formDelete import Delete
from Aplicacion.formExec import Exec
from Aplicacion.formModify import Modify
from Aplicacion.formRename import Rename
from Aplicacion.formTransfer import Transfer

from Aplicacion.Analizador.gramar import grammarInput,grammarInputCodificado
from Aplicacion.Analizador.Comandos.esencial import Leer

from tkinter import *

class MainWindow:
    def __init__(self, root):
        self.root=root
        #setting title
        self.root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        labelConsola=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=48)
        labelConsola["font"] = ft
        labelConsola["fg"] = "#333333"
        labelConsola["justify"] = "center"
        labelConsola["text"] = "Consola"
        labelConsola.place(x=10,y=50,width=279,height=45)


        



        bttnCerrar=tk.Button(self.root)
        bttnCerrar["activebackground"] = "#691111"
        bttnCerrar["anchor"] = "center"
        bttnCerrar["bg"] = "#1e90ff"
        bttnCerrar["cursor"] = "arrow"
        bttnCerrar["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        bttnCerrar["font"] = ft
        bttnCerrar["fg"] = "#ffffff"
        bttnCerrar["justify"] = "center"
        bttnCerrar["text"] = "Cerrar sesion"
        bttnCerrar["relief"] = "raised"
        bttnCerrar.place(x=470,y=420,width=115,height=41)
        bttnCerrar["command"] = self.bttnCerrar_command

        self.inputConsole=Text(self.root)
        self.inputConsole["borderwidth"] = "1px"
        self.inputConsole["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        self.inputConsole["font"] = ft
        self.inputConsole["fg"] = "#333333"
        self.inputConsole.place(x=20,y=100,width=285,height=369)

        bttnBackUp=tk.Button(self.root)
        bttnBackUp["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnBackUp["font"] = ft
        bttnBackUp["fg"] = "#ffffff"
        bttnBackUp["justify"] = "center"
        bttnBackUp["text"] = "Backup"
        bttnBackUp.place(x=330,y=350,width=115,height=45)
        bttnBackUp["command"] = self.bttnBackUp_command

        bttnCopy=tk.Button(self.root)
        bttnCopy["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnCopy["font"] = ft
        bttnCopy["fg"] = "#ffffff"
        bttnCopy["justify"] = "center"
        bttnCopy["text"] = "Copy"
        bttnCopy.place(x=330,y=280,width=115,height=45)
        bttnCopy["command"] = self.bttnCopy_command

        bttnDelete=tk.Button(self.root)
        bttnDelete["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnDelete["font"] = ft
        bttnDelete["fg"] = "#ffffff"
        bttnDelete["justify"] = "center"
        bttnDelete["text"] = "Delete"
        bttnDelete.place(x=330,y=220,width=115,height=45)
        bttnDelete["command"] = self.bttnDelete_command

        bttnCreate=tk.Button(self.root)
        bttnCreate["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnCreate["font"] = ft
        bttnCreate["fg"] = "#ffffff"
        bttnCreate["justify"] = "center"
        bttnCreate["text"] = "Create"
        bttnCreate.place(x=330,y=160,width=115,height=45)
        bttnCreate["command"] = self.bttnCreate_command

        bttnConfigure=tk.Button(self.root)
        bttnConfigure["activeforeground"] = "#ffffff"
        bttnConfigure["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        bttnConfigure["font"] = ft
        bttnConfigure["fg"] = "#ffffff"
        bttnConfigure["justify"] = "center"
        bttnConfigure["text"] = "Configure"
        bttnConfigure.place(x=330,y=100,width=115,height=45)
        bttnConfigure["command"] = self.bttnConfigure_command

        bttnExec=tk.Button(self.root)
        bttnExec["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnExec["font"] = ft
        bttnExec["fg"] = "#ffffff"
        bttnExec["justify"] = "center"
        bttnExec["text"] = "Exec"
        bttnExec.place(x=470,y=350,width=115,height=45)
        bttnExec["command"] = self.bttnExec_command

        bttnAdd=tk.Button(self.root)
        bttnAdd["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnAdd["font"] = ft
        bttnAdd["fg"] = "#ffffff"
        bttnAdd["justify"] = "center"
        bttnAdd["text"] = "Add"
        bttnAdd.place(x=470,y=280,width=115,height=45)
        bttnAdd["command"] = self.bttnAdd_command

        bttnModify=tk.Button(self.root)
        bttnModify["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnModify["font"] = ft
        bttnModify["fg"] = "#ffffff"
        bttnModify["justify"] = "center"
        bttnModify["text"] = "Modify"
        bttnModify.place(x=470,y=220,width=115,height=45)
        bttnModify["command"] = self.bttnModify_command

        bttnRename=tk.Button(self.root)
        bttnRename["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnRename["font"] = ft
        bttnRename["fg"] = "#ffffff"
        bttnRename["justify"] = "center"
        bttnRename["text"] = "Rename"
        bttnRename.place(x=470,y=160,width=115,height=45)
        bttnRename["command"] = self.bttnRename_command

        bttnTransfer=tk.Button(self.root)
        bttnTransfer["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        bttnTransfer["font"] = ft
        bttnTransfer["fg"] = "#ffffff"
        bttnTransfer["justify"] = "center"
        bttnTransfer["text"] = "Transfer"
        bttnTransfer.place(x=470,y=100,width=115,height=45)
        bttnTransfer["command"] = self.bttnTransfer_command

        bttnEjecComando=tk.Button(self.root)
        bttnEjecComando["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnEjecComando["font"] = ft
        bttnEjecComando["fg"] = "#ffffff"
        bttnEjecComando["justify"] = "center"
        bttnEjecComando["text"] = "Ejec. Comando"
        bttnEjecComando.place(x=330,y=420,width=115,height=41)
        bttnEjecComando["command"] = self.bttnEjecComando_command

    def bttnCerrar_command(self):
        self.root.destroy()

    def bttnBackUp_command(self):
        self.root = tk.Tk()
        comandoInput=BackUp(self.root)
        print(comandoInput.getInput)

    def bttnCopy_command(self):
        self.root = tk.Tk()
        comandoInput=Copy(self.root)

    def bttnDelete_command(self):
        self.root = tk.Tk()
        comandoInput=Delete(self.root)

    def bttnCreate_command(self):
        self.root = tk.Tk()
        comandoInput=Create(self.root)

    def bttnConfigure_command(self):
        self.root = tk.Tk()
        comandoInput=Configure(self.root)

    def bttnExec_command(self):
        self.root = tk.Tk()
        comandoInput=Exec(self.root)

    def bttnAdd_command(self):
        self.root = tk.Tk()
        comandoInput=Add(self.root)

    def bttnModify_command(self):
        self.root = tk.Tk()
        comandoInput=Modify(self.root)

    def bttnRename_command(self):
        self.root = tk.Tk()
        comandoInput=Rename(self.root)

    def bttnTransfer_command(self):
        self.root = tk.Tk()
        comandoInput=Transfer(self.root)

    def bttnEjecComando_command(self):
        # ESTE ES EL IMPUT DE LA CONSOLA
        #obteniendo input
        stringInput=self.inputConsole.get("1.0", "end-1c")
        #identificar si es codificado
        #Tamaño de un entrada es codificada es de 2, hexadecimal no lleva "-", los comandos si excepto para backup
        x=len(stringInput.split("\n"))
        if(x>=2):
            posibleCodificado=stringInput.split("\n")[1]# Obteniendo el posible codificado 
            if(("-" in posibleCodificado)|(posibleCodificado.lower()=="backup")):
                print(stringInput)
                grammarInput(stringInput)
            else:
                print("Codificado-------------------------------------------------------")
                print(stringInput)
                grammarInputCodificado(stringInput)
            self.inputConsole.delete("1.0","end")
        else:
            grammarInput(stringInput)




