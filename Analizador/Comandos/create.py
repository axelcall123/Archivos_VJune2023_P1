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
        self.contenido=contenido


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta

    def creacionLocal(self):
        #print(self.nombre)
        #print(self.contenido)
        #print(self.ruta)
        pathArchivo= "../Archivo/"+self.ruta.split("/")[1]
        #print(pathArchivo)
        if(os.path.exists(pathArchivo+"/"+self.nombre)==True):
            print("Archivo ya existente")
        else:
            if(os.path.exists(pathArchivo)==True):
                #existe la ruta
                f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
                f.write(self.contenido)
                f.close() # siempre cerrar
                print("archivo creado")
            else:
                #si no existe nada
                os.mkdir(pathArchivo)
                f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
                f.write(self.contenido)
                f.close() # siempre cerrar
                print("ARCHIVO CREADO")
   



        
            

        
        
    
