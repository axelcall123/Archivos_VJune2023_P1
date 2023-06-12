import os
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG
class Rename:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

    def path (self,ruta):
        
        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta
            

    def name(self,nombre):
        if('"' in nombre):
            self.nombre="/"+nombre.split("\"")[1]+"/"
        else:
            self.nombre=nombre

    def renameCloud(self):
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        if len(resultado[0]) == 0:#existe la ruta
            gC.renameCloud(servicio, resultado[1]["id"],self.nombre.replace("/",""))
            print(f"Se renombro ")
        else:
            print(f"La ruta especificada {self.ruta}, esta mal")




        
            

        
        
    

