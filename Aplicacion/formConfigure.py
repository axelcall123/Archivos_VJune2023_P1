import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

from Aplicacion.Analizador.gramar import grammarInput
from Aplicacion.Analizador.Comandos.esencial import Leer
from tkinter import messagebox as MessageBox

class Configure:
    def __init__(self, root,analizar):
        self.analizar=analizar
        self.coboGetType=""
        self.coboGetEncriptLog=""
        self.coboGetEncriptRead=""
        self.llave=""

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
        GLabel_559["text"] = "Configure"
        GLabel_559.place(x=170,y=20,width=279,height=45) 

        


        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "Type"
        GLabel_819.place(x=40,y=150,width=70,height=25)

        GLabel_577=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_577["font"] = ft
        GLabel_577["fg"] = "#333333"
        GLabel_577["justify"] = "center"
        GLabel_577["text"] = "Encrypt_log"
        GLabel_577.place(x=20,y=190,width=127,height=37)

        GLabel_824=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_824["font"] = ft
        GLabel_824["fg"] = "#333333"
        GLabel_824["justify"] = "center"
        GLabel_824["text"] = "Encrypt_read"
        GLabel_824.place(x=10,y=240,width=141,height=46)


        #GET INPUT: comboBoxType.get()
        def comboTypeFunction(event):
            self.coboGetType=comboBoxType.get()
        comboBoxType=ttk.Combobox(root,values=["Local","Cloud"])
        ft = tkFont.Font(family='Times',size=10)
        comboBoxType.place(x=170,y=150,width=340,height=30)
        comboBoxType.set("Selecciona un modo")
        comboBoxType.bind('<<ComboboxSelected>>',comboTypeFunction)

        
        
        

        def comboEncripLogFunction(event):
            self.coboGetEncriptLog=comboBoxEncripLog.get()
        comboBoxEncripLog=ttk.Combobox(root,values=["True","False"])
        ft = tkFont.Font(family='Times',size=10)
        comboBoxEncripLog.set("Selecciona un modo")
        comboBoxEncripLog.bind('<<ComboboxSelected>>',comboEncripLogFunction)
        comboBoxEncripLog.place(x=170,y=200,width=339,height=30)

        
        def comboEncripReadFunction(event):
            self.coboGetEncriptRead=comboBoxEncripRead.get()
        comboBoxEncripRead=ttk.Combobox(root,values=["True","False"])
        ft = tkFont.Font(family='Times',size=10)
        comboBoxEncripRead.set("Selecciona un modo")
        comboBoxEncripRead.bind('<<ComboboxSelected>>',comboEncripReadFunction)
        comboBoxEncripRead.place(x=170,y=250,width=337,height=30)

        GLabel_843=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_843["font"] = ft
        GLabel_843["fg"] = "#333333"
        GLabel_843["justify"] = "center"
        GLabel_843["text"] = "Llave"
        GLabel_843.place(x=30,y=310,width=93,height=34)


        # Lleva self para obtener el input
        self.inputLlave=tk.Entry(root)
        self.inputLlave["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inputLlave["font"] = ft
        self.inputLlave["fg"] = "#333333"
        self.inputLlave["justify"] = "center"
        self.inputLlave["text"] = "Entry"
        self.inputLlave.place(x=170,y=310,width=335,height=30)


        bttnEjecComando=tk.Button(root)
        bttnEjecComando["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnEjecComando["font"] = ft
        bttnEjecComando["fg"] = "#ffffff"
        bttnEjecComando["justify"] = "center"
        bttnEjecComando["text"] = "Ejec. Comando"
        bttnEjecComando.place(x=250,y=400,width=115,height=41)
        bttnEjecComando["command"] = self.bttnEjecComando_command

    
    def bttnEjecComando_command(self):
        #INPUTS DEL FORM
        #print(self.coboGetType)
        #print(self.coboGetEncriptLog)
        #print(self.coboGetEncriptRead)
        #la llave es opcional 
        if((self.coboGetEncriptRead!="")&(self.coboGetEncriptLog!="")&(self.coboGetType!="")):  
                #no se ingreso llave
                print(self.llave)
                if(self.inputLlave.get()==""):
                    stringInput="configure "+"-type->"+self.coboGetType+ " -encrypt_log->"+self.coboGetEncriptLog+" -encrypt_read->"+self.coboGetEncriptRead
                    print(stringInput)
                    grammarInput(stringInput,self.analizar)
                else:
                    stringInput="configure "+"-type->"+self.coboGetType+ "-encrypt_log->"+self.coboGetEncriptLog+" -encrypt_read->"+self.coboGetEncriptRead+" -llave->"+self.inputLlave.get()
                    print(stringInput)
                    grammarInput(stringInput,self.analizar)
        else:
            MessageBox.showerror("Error!", "Llena todos los campos")
        
        
    

if __name__ == "__main__":
    root = tk.Tk()
    Configure = Configure(root)
    root.mainloop()
