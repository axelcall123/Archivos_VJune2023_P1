from Analizador.gramar import gramarMain
from Analizador.Comandos.esencial import Leer
from Analizador.cripto import decrypt_string
from FrontEnd.SingIn import Login
import tkinter as tk
import tkinter.font as tkFont


def test():
    resultado = gramarMain("documento", "./Analizador/entradas.txt")
    analizar = Leer()
    # for res in resultado:
    #     print(res)
    analizar.comando(resultado)

def main():
    file_path ='./docs/archivo.txt'
    dicUsuario = []
    with open(file_path, 'r') as file:#leer archivo, linea a linea
        cont=0
        nombre=''
        for line in file:
            line=line.replace("\n","")
            if cont%2==0:
                nombre=line
            else:
                strDep=decrypt_string(b'miaproyecto12345', bytearray.fromhex(line))
                dicUsuario.append({"name":nombre,"pass": strDep})
            cont+=1
    print(dicUsuario)
    root = tk.Tk()
    app = Login(root,dicUsuario)
    root.mainloop()

main()
#test()