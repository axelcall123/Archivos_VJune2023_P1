import os
import shutil
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias

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

    def transferir(self):
        pathArchivofrom= "./archivos"+self.de
        pathArchivoto="./archivos"+self.a
        #print(pathArchivoto)
        #print(pathArchivofrom)
        #print(os.path.exists(pathArchivofrom)&('.' in self.de))
        #pasando archivo
        if(os.path.exists(pathArchivofrom)&('.' in self.de)):
            #mover archivo
            shutil.move(pathArchivofrom,pathArchivoto)
            print("******EL ARCHIVO FUE TRASFERIDO CON EXITO******")
        #pasando carpeta o error
        else:
            #pasando carpeta 
            if((os.path.exists(pathArchivofrom))&((os.path.exists(pathArchivoto)))):
                #existe la ruta
                #pasar todos los elementos de carpeta
                contenido = os.listdir(pathArchivofrom)
                for element in contenido:
                    #print(pathArchivofrom+element)
                    shutil.move(pathArchivofrom+element,pathArchivoto)
                #shutil.copytree(pathArchivofrom,pathArchivoto)
                print("******LA CARPETA FUE TRASFERIDA CON EXITO******")
            else:
                if(os.path.exists(pathArchivoto)):print("******ERROR LA DIRECCION YA EXISTE******")
                else:print("******ERROR NO SE ENCONTRO LA DIRECCION******")
                
    def transferCloud(self):
        retorno = gC.auxDeParaC(self.a, self.de)
        if retorno[0] == "":
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
        print(f"se tranfirieron todos los archivos")
