from Aplicacion.Analizador.gramar import gramarMain
from Aplicacion.Analizador.Comandos.esencial import Leer
from Aplicacion.SingIn import Login
from Aplicacion.Analizador.cripto import decrypt_hex_string
from Aplicacion.variablesGlobales import listaUsuarios
import tkinter as tk
import Aplicacion.Analizador.Comandos._general as _G
#pruebas
#resultado = gramarMain()
#analizar = Leer()
#analizar.comando(resultado)
#archivo=input()
archivo = "usuario.txt"
#contiene todos los usuarios con sus respectivas contraseñas
root = tk.Tk()
def callback():  # para guardar lo ultimo por si acaso, temporal
    _G.closeTempFile(True)
    root.destroy()

class Main():
    def __init__(self,):
        pass

    def login(self):
        root.protocol("WM_DELETE_WINDOW", callback)
        app = Login(root)
        root.mainloop()

    #Agregando a la lista usuarios
    def listaUsuariosFuction(self, string):
        leer = string.split("\n")
        contador = 0
        usuario = ""
        password = ""
        for element in leer:
            #identificando Usuario
            if (contador % 2 == 0):
                usuario = element
            #identificando Usuario contraseña
            elif (contador % 2 == 1):
                #desencriptando contraseñas
                #password = decrypt_hex_string(b"miaproyecto12345", bytearray.fromhex(element))
                password = decrypt_hex_string(b"miaproyecto12345", element)
                usuarios = {
                    "UserName": usuario,
                    "Password": password
                }
                print(usuarios)
                global listaUsuarios
                listaUsuarios.append(usuarios)
            contador = contador+1
        #Ejecutando login
        self.login()

    def test(self):
        resultado = gramarMain()
        analizar = Leer()
        for res in resultado:
            print(res)
        analizar.comando(resultado)

    #Obteniendo String del archivo de usuarios
    def leerUsuarios(self):
        f = open("./archivos/"+archivo, "r")  # abriendo y creando
        input = f.read()
        self.listaUsuariosFuction(input)
        _G.cerrrarTemp()
        print("BYES")

a=Main()
a.leerUsuarios()
#a.test()