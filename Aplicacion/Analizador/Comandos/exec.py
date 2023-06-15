import os
import sys


class Exec:
    def __init__ (self,):
        self.ruta=""


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta

    def ejecutarArchivo(self):
        pathArchivo= "."+self.ruta
        f = open(pathArchivo, "r")
        input = f.read()
        return input
