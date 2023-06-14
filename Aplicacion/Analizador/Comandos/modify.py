import os
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
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
        pathArchivo= "./archivos"+self.ruta
        if(os.path.exists(pathArchivo)):
            print(pathArchivo)
            f = open(pathArchivo, "w") #abriendo y creando
            f.write(self.contenido)
            f.close() # siempre cerrar
            print("******EL ARCHIVO FUE MODIFICADO CON EXITO******")
            
        else:
             print("******ERROR NO SE ENCONTRO LA DIRECCION******")
        
    def modificarCloud(self):
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        gC.escribirCloud(servicio, resultado[1]["id"], self.contenido, "")