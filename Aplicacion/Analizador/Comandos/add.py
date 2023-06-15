import os
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
from Aplicacion.variablesGlobales import temporalFile
class Add:
    def __init__ (self,):
        self.contenido=""
        self.ruta=""

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.split("\"")[1]
        else:
            self.contenido=contenido
            

    def path(self,ruta):
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta

    def aniadir(self):

        #bitacora<<<<>>>>>
        global temporalFile
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora('input', 'add',
            f'path:{"ruta"}'))
        pathArchivo= "./archivos"+self.ruta
        print(pathArchivo)
        if(os.path.exists(pathArchivo)):
            f = open(pathArchivo, "a+") #abriendo y creando
            f.write(f.read()+self.contenido)
            f.close() # siempre cerrar
            #bitacora<<<<>>>>>
            global temporalFile
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'add',
                f'se añadio el conteni al archivo con exito'))
            print("******SE AÑADIO CONTENIDO AL ARCHIVO CON EXITO******")
            
        else:
            #bitacora<<<<>>>>>
            global temporalFile
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'add',
                f'error no se encontro la direccion'))
            print("******ERROR NO SE ENCONTRO LA DIRECCION ******")
        
    def agregarCloud(self):
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        if len(resultado[0]) == 0:
            #bitacora<<<<>>>>>
            global temporalFile
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'add',
                                           f'error no se encontro la direccion'))
            print("No se econtro la ruta")
        else:
            #bitacora<<<<>>>>>
            global temporalFile
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'add',
                                           f'se añadio el conteni al archivo con exito'))
            gC.escribirCloud(servicio, resultado[1]["id"], self.contenido, "add")



        
            

        
        
    

