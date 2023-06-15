import os
import shutil
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
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
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'copy', f'from:{self.de} to:{self.a} | local')
        pathArchivofrom= "./archivos"+self.de
        pathArchivoto="./archivos"+self.a
        print(pathArchivofrom)
        print(pathArchivoto)
        print(os.path.exists(pathArchivofrom)&('.' in self.de))
        if(os.path.exists(pathArchivofrom)&('.' in self.de)):#identificando si es un archivo
            #copiar archivo
            contenido = os.listdir(pathArchivoto) # si ya existe
            for element in contenido:
                if(os.path.exists(pathArchivoto+element)):#buscar si ya existe
                    to=element.replace(".","(1).")
                    shutil.copy(pathArchivofrom,pathArchivoto+to)
                    #bitacora<<<<>>>>>
                    gG.escribirTemp('output', 'copy', 'el archivo fue copiado y renombrado con exito')
                    print("******EL ARCHIVO CON NOMBRE REPETIDO FUE COPIADO CON EXITO******")
                    return
            print("-------------")
            shutil.copy(pathArchivofrom,pathArchivoto)
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'copy', 'el archivo fue copiado con exito')
            print("******EL ARCHIVO FUE COPIADO CON EXITO******")
        else:
            if(os.path.exists(pathArchivofrom)):
                #existe la ruta
                print("--------------")
                #!--------------------------------------------
                x=len(pathArchivofrom.split("/"))
                nameModule=pathArchivofrom.split("/")[x-2]#obteniendo el nombre del modulo a copiar
                shutil.copytree(pathArchivofrom,pathArchivoto+nameModule)
                #bitacora<<<<>>>>>
                gG.escribirTemp(
                    'output', 'copy', 'la carpeta fue copiado con exito')
                print("******LA CARPETA FUE COPIADA CON EXITO******")
            else:
                #si no existe nada
                #bitacora<<<<>>>>>
                gG.escribirTemp(
                    'output', 'copy', 'no se encontro la direccion')
                print("******ERROR NO SE ENCONTRO LA DIRECCION******")

    def copiarAux(self, servicio, idA, idDe, nombre) -> str:  # para retulizar los if elif
        if gC.tipo(nombre) == "folder":  # tipo folder
            return gC.copiarCloud(servicio, idA, idDe,
                                  "application/vnd.google-apps.folder")
        elif gC.tipo(nombre) == "txt":  # tipo texto
            return gC.copiarCloud(servicio, idA, idDe,
                                  "text/plain")  # tipo txt
    def copiarCloud(self):
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'copy', f'from:{self.de} to:{self.a} | cloud')
        retorno = gC.auxDeParaC(self.a, self.de)
        if retorno[0] == "":
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'copy', 'no se encontro la direccion')
            print("no se encontro con la direccion")
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
        
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'output', 'copy', 'se copiaron todos los archivos')
        print(f"se copiaron todos los archivos")