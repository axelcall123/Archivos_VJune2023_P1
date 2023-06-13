import tkinter as tk
import tkinter.font as tkFont
from FrontEnd.ComandosForm.FormConfigure import Configure
from FrontEnd.ComandosForm.FormAdd import Add
from FrontEnd.ComandosForm.FormBackUp import BackUp
from FrontEnd.ComandosForm.FormCopy import Copy
from FrontEnd.ComandosForm.FormCreate import Create
from FrontEnd.ComandosForm.FormDelete import Delete
from FrontEnd.ComandosForm.FormExec import Exec
from FrontEnd.ComandosForm.FormModify import Modify
from FrontEnd.ComandosForm.FormRename import Rename
from FrontEnd.ComandosForm.FormTransfer import Transfer

class MainWindow:
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

        labelConsola=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        labelConsola["font"] = ft
        labelConsola["fg"] = "#333333"
        labelConsola["justify"] = "center"
        labelConsola["text"] = "Consola"
        labelConsola.place(x=10,y=50,width=279,height=45)

        bttnCerrar=tk.Button(root)
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

        inputConsole=tk.Entry(root)
        inputConsole["borderwidth"] = "1px"
        inputConsole["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        inputConsole["font"] = ft
        inputConsole["fg"] = "#333333"
        inputConsole["justify"] = "center"
        inputConsole["text"] = "Entry"
        inputConsole.place(x=20,y=100,width=285,height=369)

        bttnBackUp=tk.Button(root)
        bttnBackUp["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnBackUp["font"] = ft
        bttnBackUp["fg"] = "#ffffff"
        bttnBackUp["justify"] = "center"
        bttnBackUp["text"] = "Backup"
        bttnBackUp.place(x=330,y=350,width=115,height=45)
        bttnBackUp["command"] = self.bttnBackUp_command

        bttnCopy=tk.Button(root)
        bttnCopy["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnCopy["font"] = ft
        bttnCopy["fg"] = "#ffffff"
        bttnCopy["justify"] = "center"
        bttnCopy["text"] = "Copy"
        bttnCopy.place(x=330,y=280,width=115,height=45)
        bttnCopy["command"] = self.bttnCopy_command

        bttnDelete=tk.Button(root)
        bttnDelete["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnDelete["font"] = ft
        bttnDelete["fg"] = "#ffffff"
        bttnDelete["justify"] = "center"
        bttnDelete["text"] = "Delete"
        bttnDelete.place(x=330,y=220,width=115,height=45)
        bttnDelete["command"] = self.bttnDelete_command

        bttnCreate=tk.Button(root)
        bttnCreate["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnCreate["font"] = ft
        bttnCreate["fg"] = "#ffffff"
        bttnCreate["justify"] = "center"
        bttnCreate["text"] = "Create"
        bttnCreate.place(x=330,y=160,width=115,height=45)
        bttnCreate["command"] = self.bttnCreate_command

        bttnConfigure=tk.Button(root)
        bttnConfigure["activeforeground"] = "#ffffff"
        bttnConfigure["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        bttnConfigure["font"] = ft
        bttnConfigure["fg"] = "#ffffff"
        bttnConfigure["justify"] = "center"
        bttnConfigure["text"] = "Configure"
        bttnConfigure.place(x=330,y=100,width=115,height=45)
        bttnConfigure["command"] = self.bttnConfigure_command

        bttnExec=tk.Button(root)
        bttnExec["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnExec["font"] = ft
        bttnExec["fg"] = "#ffffff"
        bttnExec["justify"] = "center"
        bttnExec["text"] = "Exec"
        bttnExec.place(x=470,y=350,width=115,height=45)
        bttnExec["command"] = self.bttnExec_command

        bttnAdd=tk.Button(root)
        bttnAdd["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnAdd["font"] = ft
        bttnAdd["fg"] = "#ffffff"
        bttnAdd["justify"] = "center"
        bttnAdd["text"] = "Add"
        bttnAdd.place(x=470,y=280,width=115,height=45)
        bttnAdd["command"] = self.bttnAdd_command

        bttnModify=tk.Button(root)
        bttnModify["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnModify["font"] = ft
        bttnModify["fg"] = "#ffffff"
        bttnModify["justify"] = "center"
        bttnModify["text"] = "Modify"
        bttnModify.place(x=470,y=220,width=115,height=45)
        bttnModify["command"] = self.bttnModify_command

        bttnRename=tk.Button(root)
        bttnRename["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnRename["font"] = ft
        bttnRename["fg"] = "#ffffff"
        bttnRename["justify"] = "center"
        bttnRename["text"] = "Rename"
        bttnRename.place(x=470,y=160,width=115,height=45)
        bttnRename["command"] = self.bttnRename_command

        bttnTransfer=tk.Button(root)
        bttnTransfer["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        bttnTransfer["font"] = ft
        bttnTransfer["fg"] = "#ffffff"
        bttnTransfer["justify"] = "center"
        bttnTransfer["text"] = "Transfer"
        bttnTransfer.place(x=470,y=100,width=115,height=45)
        bttnTransfer["command"] = self.bttnTransfer_command

        bttnEjecComando=tk.Button(root)
        bttnEjecComando["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnEjecComando["font"] = ft
        bttnEjecComando["fg"] = "#ffffff"
        bttnEjecComando["justify"] = "center"
        bttnEjecComando["text"] = "Ejec. Comando"
        bttnEjecComando.place(x=330,y=420,width=115,height=41)
        bttnEjecComando["command"] = self.bttnEjecComando_command

    def bttnCerrar_command(self):
        root.destroy()


    def bttnBackUp_command(self):
        root = tk.Tk()
        ventana=BackUp(root)


    def bttnCopy_command(self):
        root = tk.Tk()
        ventana=Copy(root)


    def bttnDelete_command(self):
        root = tk.Tk()
        ventana=Delete(root)


    def bttnCreate_command(self):
        root = tk.Tk()
        ventana=Create(root)


    def bttnConfigure_command(self):
        root = tk.Tk()
        ventana=Configure(root)


    def bttnExec_command(self):
        root = tk.Tk()
        ventana=Exec(root)


    def bttnAdd_command(self):
        root = tk.Tk()
        ventana=Add(root)


    def bttnModify_command(self):
        root = tk.Tk()
        ventana=Modify(root)


    def bttnRename_command(self):
        root = tk.Tk()
        ventana=Rename(root)


    def bttnTransfer_command(self):
        root = tk.Tk()
        ventana=Transfer(root)


    def bttnEjecComando_command(self):
        #ejecutar el texto en el imput
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()