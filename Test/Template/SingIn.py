import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width = 452
        height = 411
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_529 = tk.Label(root)
        GLabel_529["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_529["font"] = ft
        GLabel_529["fg"] = "#333333"
        GLabel_529["justify"] = "center"
        GLabel_529["text"] = ""
        GLabel_529.place(x=60, y=40, width=300, height=323)

        GLabel_788 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_788["font"] = ft
        GLabel_788["fg"] = "#333333"
        GLabel_788["justify"] = "center"
        GLabel_788["text"] = "Sign In"
        GLabel_788.place(x=80, y=50, width=70, height=25)

        GLabel_695 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_695["font"] = ft
        GLabel_695["fg"] = "#333333"
        GLabel_695["justify"] = "center"
        GLabel_695["text"] = "User Name:"
        GLabel_695.place(x=80, y=100, width=70, height=25)

        GLabel_740 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_740["font"] = ft
        GLabel_740["fg"] = "#333333"
        GLabel_740["justify"] = "center"
        GLabel_740["text"] = "Password:"
        GLabel_740.place(x=80, y=170, width=70, height=25)

        GButton_691 = tk.Button(root)
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

        GLineEdit_330 = tk.Entry(root)
        GLineEdit_330["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_330["font"] = ft
        GLineEdit_330["fg"] = "#333333"
        GLineEdit_330["justify"] = "center"
        GLineEdit_330["text"] = "user"
        GLineEdit_330.place(x=130, y=130, width=152, height=30)

        GLineEdit_458 = tk.Entry(root)
        GLineEdit_458["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_458["font"] = ft
        GLineEdit_458["fg"] = "#333333"
        GLineEdit_458["justify"] = "center"
        GLineEdit_458["text"] = "pass"
        GLineEdit_458.place(x=130, y=210, width=146, height=30)

    def GButton_691_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
