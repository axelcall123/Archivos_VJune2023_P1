import os
import sys
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
from Aplicacion.variablesGlobales import temporalFile

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
        #bitacora<<<<>>>>>
        global temporalFile
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora('input', 'execute', f'path:{self.ruta}'))
        return input
