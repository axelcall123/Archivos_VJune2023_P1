import os
import sys

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

    def creacionLocal(self):
        print(self.nombre)
        print(self.contenido)
        print(self.ruta)
        pathArchivo= "../Archivo/"+self.ruta.split("/")[1]
        if(os.path.exists(pathArchivo)==True):
            print("Archivo ya existente")
        else:
            os.mkdir(pathArchivo)
            f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
            f.write(self.contenido)
            f.close() # siempre cerrar
   



        
            

        
        
    
