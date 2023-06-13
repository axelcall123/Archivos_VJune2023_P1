import tkinter as tk
import tkinter.font as tkFont
from FrontEnd.MainWindow import MainWindow
class Login:
    def __init__(self, root,dictado):
        self.dictado=dictado
        #setting title
        self.root = root
        self.root.title("undefined")
        #setting window size
        width = 452
        height = 411
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_529 = tk.Label(self.root)
        GLabel_529["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_529["font"] = ft
        GLabel_529["fg"] = "#333333"
        GLabel_529["justify"] = "center"
        GLabel_529["text"] = ""
        GLabel_529.place(x=60, y=40, width=300, height=323)

        GLabel_788 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_788["font"] = ft
        GLabel_788["fg"] = "#333333"
        GLabel_788["justify"] = "center"
        GLabel_788["text"] = "Sign In"
        GLabel_788.place(x=80, y=50, width=70, height=25)

        GLabel_695 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_695["font"] = ft
        GLabel_695["fg"] = "#333333"
        GLabel_695["justify"] = "center"
        GLabel_695["text"] = "User Name:"
        GLabel_695.place(x=80, y=100, width=70, height=25)

        GLabel_740 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_740["font"] = ft
        GLabel_740["fg"] = "#333333"
        GLabel_740["justify"] = "center"
        GLabel_740["text"] = "Password:"
        GLabel_740.place(x=80, y=170, width=70, height=25)

        GButton_691 = tk.Button(self.root)
        GButton_691["anchor"] = "center"
        GButton_691["bg"] = "#40b840"
        GButton_691["borderwidth"] = "0px"
        GButton_691["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        GButton_691["font"] = ft
        GButton_691["fg"] = "#ffffff"
        GButton_691["justify"] = "center"
        GButton_691["text"] = "SIGN IN"
        GButton_691.place(x=170, y=260, width=70, height=25)
        GButton_691["command"] = self.GButton_691_command


        self.GLineEdit_userName = tk.Entry(self.root)
        self.GLineEdit_userName["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_userName["font"] = ft
        self.GLineEdit_userName["fg"] = "#333333"
        self.GLineEdit_userName["justify"] = "center"
        self.GLineEdit_userName["text"] = "user"
        self.GLineEdit_userName.place(x=130, y=130, width=152, height=30)

        self.GLineEdit_passW = tk.Entry(self.root)
        self.GLineEdit_passW["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_passW["font"] = ft
        self.GLineEdit_passW["fg"] = "#333333"
        self.GLineEdit_passW["justify"] = "center"
        self.GLineEdit_passW["text"] = "pass"
        self.GLineEdit_passW.place(x=130, y=210, width=146, height=30)
            

    def GButton_691_command(self):
        strUser = self.GLineEdit_userName.get()
        strPass=self.GLineEdit_passW.get()
        logS=False
        for file in self.dictado:
            if file["name"] == strUser and file["pass"] == strPass:
                logS= True
                break
        if logS==True:
            rootS = tk.Tk()
            app = MainWindow(rootS)
            self.root.destroy()#antes del mainloop
            rootS.mainloop()
            
        else:
            print("contraseña o usuario mal")
        #print(f"command {strUser}, {strPass}")
        #self.root.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Login(root)
#     root.mainloop()
