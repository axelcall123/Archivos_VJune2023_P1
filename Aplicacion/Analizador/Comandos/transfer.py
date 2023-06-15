import os
import shutil
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
from Aplicacion.variablesGlobales import temporalFile
class Transfer:
    def __init__ (self,):
        self.de=""
        self.a=""
        self.modo=""

    def desde (self,de):
        if('"' in de):
            self.de="/"+de.split("\"")[1]+"/"
        else:
            self.de=de

    def to(self,a):
        if('"' in a):
            self.a="/"+a.split("\"")[1]+"/"
        else:
            self.a=a

    def mode(self,mode):
        if('"' in mode):
            self.modo=mode.split("\"")[1]
        else:
            self.modo=mode

    def transferir(self):#FIXME: es por self.mode
        #bitacora<<<<>>>>>
        global temporalFile
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora('input', 'transfer', f'from: {self.desde} to: {self.a} | {self.mode}'))
        pathArchivofrom= "./archivos"+self.de
        pathArchivoto="./archivos"+self.a
        print(pathArchivoto)
        print(pathArchivofrom)
        print(os.path.exists(pathArchivofrom)&('.' in self.de))
        #pasando archivo
        if(os.path.exists(pathArchivofrom)&('.' in self.de)):
            contenido = os.listdir(pathArchivoto) # si ya existe
            for element in contenido:
                if(os.path.exists(pathArchivoto+element)):#buscar si ya existe
                    to=element.replace(".","(1).")
                    shutil.copy(pathArchivofrom,pathArchivoto+to)
                    temporalFile = tempfile.TemporaryFile()
                    temporalFile.write(gG.bitacora('output', 'transfer', 'el archivo fue transferido y renombrado con exito'))
                    print("******EL ARCHIVO CON NOMBRE REPETIDO FUE COPIADO CON EXITO******")
                    return
            #mover archivo
            print("-----------------------------")
            shutil.move(pathArchivofrom,pathArchivoto)
            #bitacora<<<<>>>>>
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'transfer','el archivo fue trasnferido con exito'))
            print("******EL ARCHIVO FUE TRASFERIDO CON EXITO******")
        #pasando carpeta o error
        else:
            #pasando carpeta 
            if((os.path.exists(pathArchivofrom))&((os.path.exists(pathArchivoto)))):
                #existe la ruta
                #pasar todos los elementos de carpeta
                contenido = os.listdir(pathArchivofrom)
                for element in contenido:
                    if((not(os.path.exists(pathArchivoto+element)))):
                        #print(pathArchivofrom+element)
                        #print(pathArchivoto)
                        shutil.move(pathArchivofrom+element,pathArchivoto)
                    else:
                        #bitacora<<<<>>>>>
                        temporalFile = tempfile.TemporaryFile()
                        temporalFile.write(gG.bitacora('output', 'transfer', 'ya exite'))
                        
                        to=element.replace(".","(1).")
                        #print(pathArchivoto+to)
                        shutil.move(pathArchivofrom+element,pathArchivoto+to)
                        print("*****YA EXISTE*******")
                        
                #bitacora<<<<>>>>>
                temporalFile = tempfile.TemporaryFile()
                temporalFile.write(gG.bitacora('output', 'transfer', 'la carpeta fue transferida con exito'))
                print("******LA CARPETA FUE TRASFERIDA CON EXITO******")
            else:               
                if(os.path.exists(pathArchivoto)):
                    #bitacora<<<<>>>>>
                    temporalFile = tempfile.TemporaryFile()
                    temporalFile.write(gG.bitacora('output', 'transfer', 'la dierccion ya exite'))
                    print("******ERROR LA DIRECCION YA EXISTE******")
                else:
                    #bitacora<<<<>>>>>
                    temporalFile = tempfile.TemporaryFile()
                    temporalFile.write(gG.bitacora(
                        'output', 'transfer', 'no se encontro la direccion'))
                    print("******ERROR NO SE ENCONTRO LA DIRECCION******")
                
    def transferCloud(self):
        #bitacora<<<<>>>>>
        global temporalFile
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora('input', 'transfer',f'from: {self.desde} to: {self.a} | {self.mode}'))
        retorno = gC.auxDeParaC(self.a, self.de)
        if retorno[0] == "":
            #bitacora<<<<>>>>>
            temporalFile = tempfile.TemporaryFile()
            temporalFile.write(gG.bitacora('output', 'transfer', 'no se encontro la direccion'))
            print("error en la direc")
            return
        servicio = gC.servicioCloud()
        idA = retorno[0]
        idDe = retorno[1]
        response = servicio.files().get(
            fileId=idDe, fields='name, mimeType').execute()  # DOBLEX2
        # respuesta=gC.existeNombreC(servicio,idA,response["name"])
        # if respuesta["existe"]=="false":#solo copio
        #     gC.tranferCloud(servicio, idA, idDe)
        # else:
        reName = gC.creRenameC(servicio, idA, response["name"])
        gC.tranferCloud(servicio, idA, idDe)
        if response["name"] != reName:  # nuevo nombre, para renombrar
            gC.renameCloud(servicio, idDe, reName)
        #bitacora<<<<>>>>>
        temporalFile = tempfile.TemporaryFile()
        temporalFile.write(gG.bitacora(
                'output', 'transfer', 'los archivos fueron transferidos con exito'))
        print(f"se tranfirieron todos los archivos")
