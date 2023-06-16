import tkinter as tk
import tkinter.font as tkFont


from Aplicacion.Analizador.gramar import grammarInput
from tkinter import messagebox as MessageBox

class Modify:
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
        GLabel_559["text"] = "Modify"
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
        GLabel_819["text"] = "Path"
        GLabel_819.place(x=70,y=150,width=70,height=25)

        GLabel_824=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_824["font"] = ft
        GLabel_824["fg"] = "#333333"
        GLabel_824["justify"] = "center"
        GLabel_824["text"] = "Body"
        GLabel_824.place(x=30,y=220,width=141,height=46)

        self.path=tk.Entry(root)
        self.path["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.path["font"] = ft
        self.path["fg"] = "#333333"
        self.path["justify"] = "center"
        self.path.place(x=170,y=150,width=337,height=30)

        self.body=tk.Entry(root)
        self.body["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.body["font"] = ft
        self.body["fg"] = "#333333"
        self.body["justify"] = "center"
        self.body.place(x=170,y=230,width=338,height=30)

    def GButton_364_command(self):
        #print(self.path.get())
        #print(self.body.get())
        if((self.path.get()!="")&(self.body.get()!="")):  
            stringInput="modify "+ "-path->"+self.path.get()+" -body->"+self.body.get()
            print(stringInput)
            grammarInput(stringInput)
        else:
            MessageBox.showerror("Error!", "Llena todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    Modify = Modify(root)
    root.mainloop()
