import os
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG
class Delete:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

    def path (self,ruta):

        if('"' in ruta):
            self.ruta=ruta.split("\"")[1]
        else:
            self.ruta=ruta

    def name(self,nombre):
        if('"' in nombre):
            self.nombre=nombre.split("\"")[1]
        else:
            self.nombre=nombre

    def borrar(self):
        pathArchivo= "../Archivo"+self.ruta
        if(os.path.exists(pathArchivo+self.nombre)&(self.nombre!="")):
            os.remove(pathArchivo+self.nombre)
            print("******EL ARCHIVO FUE BORRADO CON EXITO******")
        else:
            if(os.path.exists(pathArchivo)):
                self.elementosDirectorio(pathArchivo)
                os.rmdir(pathArchivo)
                print("******LA CARPETA FUE BORRADO CON EXITO******")
            else:
                #si no existe nada
                 print("******ERROR NO SE ENCONTRO LA DIRECCION******")
        
    def elementosDirectorio(self,path):
        contenido = os.listdir(path)
        print(contenido)
        print(contenido==[])
        if(contenido==[]):
            return
        else:
            for element in contenido:
                if("." in element):
                    os.remove(path+"/"+element)
                    print("*****SE ELIMINO EL ARCHIVO DENTRO DE CARPETA: "+path+element)
                else:
                    contenido2=os.listdir(path+element)
                    if(contenido2==[]):
                        os.rmdir(path+element)
                        print("*****SE ELIMINO EL CARPETA DENTRO DE CARPETA: "+path+element)
                    else:
                        self.elementosDirectorio(path+element)

            
            
    def borrarCloud(self):
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        if len(resultado[0]) == 0:  # llegue al final de las carpetas
            if self.nombre == "":  # es una carpeta que se elminina
                gC.eliminarCloud(servicio, resultado[1]["id"], 'folder')
            else:  # es una archivo que se elminina
                res = gC.existeNombreC(
                    servicio, resultado[1]["id"], self.nombre)
                if res["existe"] == "true":  # existe archivo que elminar
                    gC.eliminarCloud(servicio, res["id"], 'txt')
                else:
                    print("Indico mal el nombre del archivo vuelva a intentarlo")

        else:  # url mala
            print(f"La ruta especificada {self.ruta}, esta mal")




        
            

        
        
    

