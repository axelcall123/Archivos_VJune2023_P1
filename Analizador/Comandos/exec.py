import os
import sys

class Exec:
    def __init__ (self,):
        self.ruta=""


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta=ruta.split("\"")[1]
        else:
            self.ruta=ruta

    def ejecutarArchivo(self):
        ruta="."+self.ruta
        #f = open("./archivos/calificacion.mia", "r")
        f = open(ruta, "r")
        input = f.read()
        print("RETORNANDO CONTENIDO ARCHIVO.MIA")
        return input
   



        
            

        
        
    