import os
import shutil
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
class Copy:
    def __init__ (self,):
        self.de=""
        self.a=""

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

    def copiar(self):
        pathArchivofrom= "./archivos"+self.de
        pathArchivoto="./archivos"+self.a
        print(pathArchivofrom)
        print(pathArchivoto)
        print(os.path.exists(pathArchivofrom)&('.' in self.de))
        if(os.path.exists(pathArchivofrom)&('.' in self.de)):
            #copiar archivo
            shutil.copy(pathArchivofrom,pathArchivoto)
            print("******EL ARCHIVO FUE COPIADO CON EXITO******")
        else:
            if(os.path.exists(pathArchivofrom)):
                #existe la ruta
                print("--------------")
                #!--------------------------------------------
                shutil.copytree(pathArchivofrom,pathArchivoto)
                print("******LA CARPETA FUE COPIADA CON EXITO******")
            else:
                #si no existe nada
                 print("******ERROR NO SE ENCONTRO LA DIRECCION******")
       
    def copiarCloud(self):
        retorno = gC.auxDeParaC(self.a, self.de)
        if retorno[0] == "":
            return
        servicio = gC.servicioCloud()
        idA = retorno[0]
        idDe = retorno[1]

        listadoDe = gC.listadoCloud(servicio, idDe)  # contiene de
        response = servicio.files().get(
            fileId=idDe, fields='name, mimeType').execute()  # DOBLEX2
        # si es txt, no obtendre diccionario, agrego solo un diccionario
        if response['mimeType'] == "text/plain":
            listadoDe.append(
                {'mimeType': 'text/plain', 'id': idDe, 'name': response['name']})

        for file in listadoDe:  # listado de archivos que copiar, ver si existe el mismo nombre
            reNombre = gC.creRenameC(servicio, idA, file["name"])
            if reNombre == file["name"]:  # nombre es igual solo copiar
                self.copiarAux(servicio, idA, file["id"], file["name"])
            else:  # otro nombre diferente
                idN = self.copiarAux(
                    servicio, idA, file["id"], file["name"])  # copio
                gC.renameCloud(servicio, idN, reNombre)  # renombre el copiado
        print(f"se copiaron todos los archivos")






        
            

        
        
    

