import os
import sys
import Analizador.Comandos._generalCloud as gC# alias
import Analizador.Comandos._general as gG
class Create:
    def __init__ (self,):
        self.nombre=""
        self.contenido=""
        self.ruta=""

    def name (self,nombre):
        #posibles cambios necesario al nombre
        if('"' in nombre):
            self.nombre=nombre.split("\"")[1]
        else:
            self.nombre=nombre
        
        

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.split("\"")[1]
        else:
            self.contenido=contenido


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta

    
    
    
    
    
    
    
    
    
    
    def creacionCloud(self):
        #print('ver')
        #print(self.nombre, self.contenido, self.ruta)
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado=gC.navegacionCarpetasC(servicio, arrayRuta,'1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')#navego lo maximo posible
        if len(resultado[0])!=0:#no navego hasta el final de la carpeta, crear carpetas restantes
            res=gC.creacionCarpetaIteraC(servicio, resultado[0], resultado[1]["id"])
            gC.crearCloud(servicio, self.nombre, 'text/plain',res,self.contenido)
        else:#crear archivo
            rename = gC.creRenameC(servicio, resultado[1]["id"], self.nombre)
            gC.crearCloud(servicio, rename,
                          'text/plain', resultado[1]["id"],self.contenido)
        return
