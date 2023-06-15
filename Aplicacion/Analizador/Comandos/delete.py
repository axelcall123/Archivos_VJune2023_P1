import os
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
from Aplicacion.variablesGlobales import temporalFile
class Delete:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

        self.num=0

    def path (self,ruta):

        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta

    def name(self,nombre):
        if('"' in nombre):
            self.nombre=nombre.replace("\"", "" )
        else:
            self.nombre=nombre

    def borrar(self):
        #bitacora<<<<>>>>>
        global temporalFile
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora('input', 'delete', f'path:{self.ruta} name:{self.nombre} | local'))
        pathArchivo= "./archivos"+self.ruta
        #print(pathArchivo+self.nombre)
        
        #Existe direccion completa
        #print(os.path.exists(pathArchivo+self.nombre)&(self.nombre!=""))
        if(os.path.exists(pathArchivo+self.nombre)&(self.nombre!="")):
            os.remove(pathArchivo+self.nombre)
            #bitacora<<<<>>>>>
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'delete','el archivo fue borrado'))
            print("******EL ARCHIVO FUE BORRADO CON EXITO******")
        else:
            #existe solo path
            if(os.path.exists(pathArchivo)&(self.nombre=="")):
                x=0
                self.elementosDirectorio(pathArchivo)
                while x<=self.num:
                    self.elementosDirectorio(pathArchivo)
                    #print(x)
                    x=x+1
                os.rmdir(pathArchivo)
                #bitacora<<<<>>>>>
                temporalFile = tempfile.TemporaryFile()
                temporalFile.write(gG.bitacora('output', 'delete', 'la carpeta fue borrada'))
                print("******LA CARPETA FUE BORRADO CON EXITO******")
            else:
                #si no existe nada
                #bitacora<<<<>>>>>
                temporalFile = tempfile.TemporaryFile()
                temporalFile.write(gG.bitacora('output', 'delete', 'no se encontro la direccion'))
                print("******ERROR NO SE ENCONTRO LA DIRECCION******")
        
    def elementosDirectorio(self,path):
        contenido = os.listdir(path)
        #print(contenido)
        if(contenido==[]):
            return 
        else:
            for element in contenido:
                #SI ES ARCHIVO
                if("." in element):
                    os.remove(path+"/"+element)
                    print("*****SE ELIMINO EL ARCHIVO DENTRO DE CARPETA: "+path+element)
                #SI ES CARPETA
                else:
                    contenido2=os.listdir(path+element)
                    print(contenido2)
                    if(contenido2==[]):
                        print(path+element)
                        os.rmdir(path+element)
                        print("*****SE ELIMINO EL CARPETA DENTRO DE CARPETA: "+path+element)
                    else:
                        self.num=self.num+1
                        self.elementosDirectorio(path+element+"/")

    def borrarCloud(self):
        #bitacora<<<<>>>>>
        global temporalFile
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora('input', 'delete',f'path:{self.ruta} name:{self.nombre} | cloud'))
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        if len(resultado[0]) == 0:  # llegue al final de las carpetas
            if self.nombre == "":  # es una carpeta que se elminina
                gC.eliminarCloud(
                    servicio, resultado[1]["id"], 'application/vnd.google-apps.folder')
            else:  # es una archivo que se elminina
                res = gC.existeNombreC(
                    servicio, resultado[1]["id"], self.nombre)
                if res["existe"] == "true":  # existe archivo que elminar
                    gC.eliminarCloud(servicio, res["id"], 'text/plain')
                    #bitacora<<<<>>>>>
                    temporalFile = tempfile.TemporaryFile()
                    temporalFile.write(gG.bitacora('output', 'delete', 'se elimino todo'))
                    print("termino de elminar todo")
                    return
                else:
                    #bitacora<<<<>>>>>
                    temporalFile = tempfile.TemporaryFile()
                    temporalFile.write(gG.bitacora('output', 'delete', 'indico mal el nombre'))
                    print("Indico mal el nombre del archivo vuelva a intentarlo")
                    return

        else:  # url mala
            #bitacora<<<<>>>>>
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'delete', 'no se encontro la direccion'))
            print(f"La ruta especificada {self.ruta}, esta mal")
            return
        



        
            

        
        
    

