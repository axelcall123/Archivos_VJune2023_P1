import os
import shutil
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
class Transfer:
    def __init__ (self,):
        self.de=""
        self.a=""
        self.modo=""

    def desde (self,de):
        if('"' in de):
            self.de=de.replace("\"", "" )
        else:
            self.de=de

    def to(self,a):
        if('"' in a):
            self.a=a.replace("\"", "" )
        else:
            self.a=a

    def mode(self,mode):
        if('"' in mode):
            self.modo=mode.replace("\"", "" )
        else:
            self.modo=mode

    def transferir(self):#FIXME: es por self.mode
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'transfer', f'from: {self.de} to: {self.a} | {self.mode}')
        pathArchivofrom= "./archivos"+self.de
        pathArchivoto="./archivos"+self.a
        print(pathArchivoto)
        print(pathArchivofrom)
        print(os.path.exists(pathArchivofrom)&('.' in self.de))
        #pasando archivo
        if(os.path.exists(pathArchivofrom)&('.' in self.de)):
            contenido = os.listdir(pathArchivoto) # si ya existe
            x=len(pathArchivofrom.split("/"))
            namFile=pathArchivofrom.split("/")[x-1]
            for element in contenido:
                if(os.path.exists(pathArchivoto+element)&(element==namFile)):#buscar si ya existe
                    to=element.replace(".","(1).")
                    shutil.copy(pathArchivofrom,pathArchivoto+to)
                    #bitacora<<<<>>>>>
                    gG.escribirTemp(
                        'output', 'transfer', 'el archivo fue transferido y renombrado con exito')
                    print("******EL ARCHIVO CON NOMBRE REPETIDO FUE COPIADO CON EXITO******")
                    return
            #mover archivo
            print("-----------------------------")
            shutil.move(pathArchivofrom,pathArchivoto)
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'transfer', 'el archivo fue trasnferido con exito')
            print("******EL ARCHIVO FUE TRASFERIDO CON EXITO******")
        #pasando carpeta o error
        else:
            #pasando carpeta 
            if((os.path.exists(pathArchivofrom))&((os.path.exists(pathArchivoto)))):
                x=len(pathArchivofrom.split("/"))
                nameModule=pathArchivofrom.split("/")[x-2]#obteniendo el nombre del modulo a copiar
                contenido = os.listdir(pathArchivoto) # si ya existe
                for element in contenido:
                    if(os.path.exists(pathArchivoto+nameModule)):
                        to=nameModule+"(1)"
                        print(pathArchivoto+to)
                        shutil.move(pathArchivofrom,pathArchivoto+to)
                        #bitacora<<<<>>>>>
                        gG.escribirTemp(
                            'output', 'transfer', 'la carpeta fue transferida y renombrada con exito')
                        print("******LA CARPETA FUE TRASFERIDA CON EXITO******")
                        return                
                
                shutil.move(pathArchivofrom,pathArchivoto+nameModule)
                #bitacora<<<<>>>>>
                gG.escribirTemp(
                    'output', 'transfer', 'la carpeta fue transferida con exito')
                print("******LA CARPETA FUE TRASFERIDA CON EXITO******")

            #error
            else:               
                    #bitacora<<<<>>>>>
                    gG.escribirTemp(
                        'output', 'transfer', 'no se encontro la direccion')
                    print("******ERROR NO SE ENCONTRO LA DIRECCION******")
                
    def transferCloud(self):
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'transfer', f'from: {self.de} to: {self.a} | {self.mode}')
        retorno = gC.auxDeParaC(self.a, self.de)
        if retorno[0] == "":
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'transfer', 'no se encontro la direccion')
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
        gG.escribirTemp(
                'output', 'transfer', 'los archivos fueron transferidos con exito')
        print(f"se tranfirieron todos los archivos")
