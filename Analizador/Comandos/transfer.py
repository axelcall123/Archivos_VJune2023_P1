import os
import shutil
import Analizador.Comandos._generalCloud as gC  # alias

class Transfer:
    def __init__(self,):
        self.de = ""
        self.a = ""
        self.modo = ""

    def desde(self, de):
        if ('"' in de):
            self.de = de.split("\"")[1]
        else:
            self.de = de

    def to(self, a):
        if ('"' in a):
            self.a = a.split("\"")[1]
        else:
            self.a = a

    def mode(self, mode):
        if ('"' in mode):
            self.modo = mode.split("\"")[1]
        else:
            self.modo = mode

    def transferir(self):
        pathArchivofrom = "./archivos"+self.de
        pathArchivoto = "./archivos"+self.a
        print(pathArchivofrom)
        print(pathArchivoto)
        print(os.path.exists(pathArchivofrom))
        if (os.path.exists(pathArchivofrom) & ('.' in pathArchivofrom)):
            #mover archivo
            shutil.move(pathArchivofrom, pathArchivoto)
            print("******EL ARCHIVO FUE TRASFERIDO CON EXITO******")
        else:
            if (os.path.exists(pathArchivofrom) & (not (os.path.exists(pathArchivoto)))):
                #existe la ruta
                shutil.copytree(pathArchivofrom, pathArchivoto)
                print("******LA CARPETA FUE TRASFERIDA CON EXITO******")
            else:
                #si no existe nada
                if (os.path.exists(pathArchivoto)):
                    print("******ERROR LA DIRECCION YA EXISTE******")
                else:
                    print("******ERROR NO SE ENCONTRO LA DIRECCION******")
       
            
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
        if response["name"] != reName:#nuevo nombre, para renombrar
            gC.renameCloud(servicio, idDe, reName)
        print(f"se tranfirieron todos los archivos")
