import os
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
class Modify:
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

    def modificar(self):
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'modify', f'path:{self.ruta}')
        pathArchivo= "./archivos"+self.ruta
        if(os.path.exists(pathArchivo)):
            print(pathArchivo)
            f = open(pathArchivo, "w") #abriendo y creando
            f.write(self.contenido)  # <<<<<here proces file
            gG.archivosProcesados(0, 1, 0, 0)
            f.close() # siempre cerrar
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'modify', 'el archivo fue modificado con exito')
            print("******EL ARCHIVO FUE MODIFICADO CON EXITO******")
            
        else:
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'modify', 'no se econtro la direccion')
            print("******ERROR NO SE ENCONTRO LA DIRECCION******")
        
    def modificarCloud(self):
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'modify', f'path:{self.ruta}')
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        if len(resultado[0]) != 0:  # llegue al final de las carpetas/de
            gC.escribirCloud(servicio, resultado[1]["id"], self.contenido, "")
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'modify', 'el archivo fue modificado con exito')
            print("el archivo fue modificado")
        else:
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'modify', 'no se econtro la direccion')
            print("ruta mala")