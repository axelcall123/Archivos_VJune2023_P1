import os
import sys

class Create:
    def __init__ (self,):
        self.nombre=""
        self.contenido=""
        self.ruta=""
    def name (self,nombre):
        #posibles cambios necesario al nombre
        self.nombre=nombre

    def body (self,contenido):
        self.contenido=contenido

    def path (self,ruta):
        #posibles cambios necesario ala ruta
        self.ruta=ruta

    def creacionLocal(self):
        #print(self.nombre)
        #print(self.contenido)
        #print(self.ruta)
        pathArchivo= "../Archivo/"+self.ruta.split("/")[1]
        if(os.path.exists(pathArchivo)==True):
            print("Archivo ya existente")
        else:
            os.mkdir(pathArchivo)
            f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
            f.write(self.contenido)
            f.close() # siempre cerrar
   



        
            

        
        
    
