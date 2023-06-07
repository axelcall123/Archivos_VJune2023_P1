import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("mainWindow")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_559=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_559["font"] = ft
        GLabel_559["fg"] = "#333333"
        GLabel_559["justify"] = "center"
        GLabel_559["text"] = "Consola"
        GLabel_559.place(x=10,y=50,width=279,height=45)

        GButton_489=tk.Button(root)
        GButton_489["activebackground"] = "#691111"
        GButton_489["anchor"] = "center"
        GButton_489["bg"] = "#1e90ff"
        GButton_489["cursor"] = "arrow"
        GButton_489["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_489["font"] = ft
        GButton_489["fg"] = "#ffffff"
        GButton_489["justify"] = "center"
        GButton_489["text"] = "Cerrar sesion"
        GButton_489["relief"] = "raised"
        GButton_489.place(x=330,y=430,width=115,height=41)
        GButton_489["command"] = self.GButton_489_command

        GLineEdit_89=tk.Entry(root)
        GLineEdit_89["borderwidth"] = "1px"
        GLineEdit_89["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_89["font"] = ft
        GLineEdit_89["fg"] = "#333333"
        GLineEdit_89["justify"] = "center"
        GLineEdit_89["text"] = "Entry"
        GLineEdit_89.place(x=20,y=100,width=285,height=369)

        GButton_367=tk.Button(root)
        GButton_367["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_367["font"] = ft
        GButton_367["fg"] = "#ffffff"
        GButton_367["justify"] = "center"
        GButton_367["text"] = "Backup"
        GButton_367.place(x=330,y=340,width=115,height=45)
        GButton_367["command"] = self.GButton_367_command

        GButton_721=tk.Button(root)
        GButton_721["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_721["font"] = ft
        GButton_721["fg"] = "#ffffff"
        GButton_721["justify"] = "center"
        GButton_721["text"] = "Copy"
        GButton_721.place(x=330,y=280,width=115,height=45)
        GButton_721["command"] = self.GButton_721_command

        GButton_10=tk.Button(root)
        GButton_10["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_10["font"] = ft
        GButton_10["fg"] = "#ffffff"
        GButton_10["justify"] = "center"
        GButton_10["text"] = "Delete"
        GButton_10.place(x=330,y=220,width=115,height=45)
        GButton_10["command"] = self.GButton_10_command

        GButton_779=tk.Button(root)
        GButton_779["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#ffffff"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "Create"
        GButton_779.place(x=330,y=160,width=115,height=45)
        GButton_779["command"] = self.GButton_779_command

        GButton_805=tk.Button(root)
        GButton_805["activeforeground"] = "#ffffff"
        GButton_805["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_805["font"] = ft
        GButton_805["fg"] = "#ffffff"
        GButton_805["justify"] = "center"
        GButton_805["text"] = "Configure"
        GButton_805.place(x=330,y=100,width=115,height=45)
        GButton_805["command"] = self.GButton_805_command

        GButton_175=tk.Button(root)
        GButton_175["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_175["font"] = ft
        GButton_175["fg"] = "#ffffff"
        GButton_175["justify"] = "center"
        GButton_175["text"] = "Exec"
        GButton_175.place(x=470,y=340,width=115,height=45)
        GButton_175["command"] = self.GButton_175_command

        GButton_191=tk.Button(root)
        GButton_191["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_191["font"] = ft
        GButton_191["fg"] = "#ffffff"
        GButton_191["justify"] = "center"
        GButton_191["text"] = "Add"
        GButton_191.place(x=470,y=280,width=115,height=45)
        GButton_191["command"] = self.GButton_191_command

        GButton_63=tk.Button(root)
        GButton_63["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_63["font"] = ft
        GButton_63["fg"] = "#ffffff"
        GButton_63["justify"] = "center"
        GButton_63["text"] = "Modify"
        GButton_63.place(x=470,y=220,width=115,height=45)
        GButton_63["command"] = self.GButton_63_command

        GButton_390=tk.Button(root)
        GButton_390["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_390["font"] = ft
        GButton_390["fg"] = "#ffffff"
        GButton_390["justify"] = "center"
        GButton_390["text"] = "Rename"
        GButton_390.place(x=470,y=160,width=115,height=45)
        GButton_390["command"] = self.GButton_390_command

        GButton_485=tk.Button(root)
        GButton_485["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_485["font"] = ft
        GButton_485["fg"] = "#ffffff"
        GButton_485["justify"] = "center"
        GButton_485["text"] = "Transfer"
        GButton_485.place(x=470,y=100,width=115,height=45)
        GButton_485["command"] = self.GButton_485_command

    def GButton_489_command(self):
        print("command")


    def GButton_367_command(self):
        print("command")


    def GButton_721_command(self):
        print("command")


    def GButton_10_command(self):
        print("command")


    def GButton_779_command(self):
        print("command")


    def GButton_805_command(self):
        print("command")


    def GButton_175_command(self):
        print("command")


    def GButton_191_command(self):
        print("command")


    def GButton_63_command(self):
        print("command")


    def GButton_390_command(self):
        print("command")


    def GButton_485_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
