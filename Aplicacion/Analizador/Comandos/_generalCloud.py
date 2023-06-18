from typing import List,Tuple
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaInMemoryUpload
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
import Aplicacion.Analizador.Comandos._general as gG

def servicioCloud():
    scopes = [
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive'  # carpeta
    ]
    creds = None
    #print("path TF", os.path.exists('token.json'))
    if os.path.exists('token.json'):  # crea un archivo, si no existe con las credenciales
        creds = Credentials.from_authorized_user_file(
            'token.json', scopes)  # leer archivos
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Test\credentials.json',
                scopes)  # se le entrega todos las credenciales
            creds = flow.run_local_server(port=0)
        # guarda las credenciales par el siguiente arranque
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # acceso a la nube,buscar,subir
        return build('drive', 'v3', credentials=creds)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'a ocurrido un error: {error}')

def listadoCloud(service,idFolderRaiz:str)->List[dict]:#retorna listado normal
    resultado = service.files().list(
        q=f"'{idFolderRaiz}' in parents and trashed=false",
        fields="files(id, name, mimeType)").execute()
    return resultado.get('files', [])#retorna listado
    
def existeNombreC(service,idFolderRaiz:str,nombre:str)->dict:# saber si existe una carpeta u archivo igual
    files=listadoCloud(service,idFolderRaiz)
    #EXISTE nombre:
    if not files:
        return {'existe': "false", "id": idFolderRaiz,"name":nombre}
    else:
        for file in files:
            if file['name'] == nombre: 
                return {'existe': "true", "id": file['id'], "name": file["name"]}
            
        return {'existe': "false", "id": idFolderRaiz, "name": nombre}
    

def tipo(nombre:str)->str:#devuelve el tipo que es, folder o archivo
    arr = nombre.split(".")
    if len(arr) == 1:
        return "folder"
    elif len(arr) == 2:
        return arr[1]

def crearCloud(service, nombre:str, tipo:str, idFolderRaiz:str,contenido:str)->str:#crea carpeta|archivo
    metadata = {
        'name': nombre,
        'mimeType': tipo,
        'parents': [idFolderRaiz]
    }
    if tipo == 'text/plain':#creo txt
        media = MediaInMemoryUpload(
            contenido.encode(),
            mimetype='text/plain',
            resumable=True
        )
        archivo = service.files().create(
            body=metadata,
            media_body=media,
            fields='id'
        ).execute()  # <<<<<here proces file
        gG.archivosProcesados(1,0,0,0)
        print(f'creando archivo: {nombre}')
        return archivo.get("id")
    elif tipo == 'application/vnd.google-apps.folder':#creo folder
        folder = service.files().create(
        body=metadata, fields='id').execute()
        print(f'creando folder: {nombre}')
        return folder.get("id")

def navegacionCarpetasC(service,arrayCarpetas:List[str],idFolderRaiz:str)->list[list[str],dict]:#[car1,car2,car3,txt.txt]
    while len(arrayCarpetas) != 0:  # solo quede txt.txt
        json = existeNombreC(service, idFolderRaiz, arrayCarpetas[0])
        if json['existe'] == 'true':  # existe carpeta|archivo
            quetipo = tipo(arrayCarpetas[0])
            if quetipo == "folder":#sigo navegando
                arrayCarpetas.pop(0)
                return navegacionCarpetasC(service, arrayCarpetas,json["id"])
            elif quetipo=="txt":#llegue al final de la url, solo queda txt [txt.txt], con nombre igual
                arrayCarpetas.pop(0)
                json={"Tipo":"txt","Same":"True","id":json["id"],"name":json["name"]}
                #json={"Tipo":"txt","Same":"True","id":json["id"]}
                return [arrayCarpetas,json]
            else:
                print()
        else:#no existe carpeta o archivo
            quetipo = tipo(arrayCarpetas[0])
            if quetipo == "folder":  #llegue al final de mi navegacion en carpetas, [carn,..,txt.txt]|
                json = {"Tipo": "folder", "Same": "",
                        "id": json["id"], "name": json["name"]}
                return [arrayCarpetas, json]
            elif quetipo=="txt":# llegue al final del txt [txt.txt], sin nombre igual
                json = {"Tipo": "txt", "Same": "False",
                        "id": json["id"], "name": json["name"]}
                return [arrayCarpetas, json]
            else:
                print()
    folder = service.files().get(fileId=idFolderRaiz, fields='name').execute()#obtengo el nombre del >
    json = {"Tipo": "folder", "Same": "",
            "id": idFolderRaiz, "name": folder["name"]}
    return [arrayCarpetas, json]

def creRenameC(service,idFolderRaiz:str,nombre:str)->str:  # crea el nombre carpeta|archivo que se quiere crear, si existe el nombre repetido
    resutado=existeNombreC(service, idFolderRaiz, nombre)#FIXME: para no reahacerlo se puede poner otro parametro par unirlo con navacion carpetas, se puede optimizar
    if resutado["existe"]=="true":#existe nombre
        array=nombre.split(".")
        if len(array)==1:#para folder
            nombre=nombre+'(1)'
        else:#para extension
            nombre=array[0]+'(1).'+array[1]#
        return creRenameC(service, idFolderRaiz,nombre)
    else:#no existe nombre, retorno el nombre
        return nombre


# crea el nombre carpeta|archivo que se quiere crear, si existe el nombre repetido
def creRenameL(idFolderRaiz: str, nombre: str) -> str:
    # FIXME: para no reahacerlo se puede poner otro parametro par unirlo con navacion carpetas, se puede optimizar
    if os.path.exists(idFolderRaiz+'/'+nombre):  # existe nombre
        array = nombre.split(".")
        if len(array) == 1:  # para folder
            nombre = nombre+'(1)'
        else:  # para extension
            nombre = array[0]+'(1).'+array[1]
        return creRenameL(idFolderRaiz, nombre)
    else:  # no existe nombre, retorno el nombre
        return nombre

def creacionCarpetaIteraC(service, array: list[str], idFolder: str) -> str:
    while len(array) != 0:
        idFolder=crearCloud(
            service, array[0], 'application/vnd.google-apps.folder', idFolder, '')
        array.pop(0)
        return creacionCarpetaIteraC(service, array, idFolder)
    return idFolder

def eliminarCloud(service, idDelete:str,tipo):
    service.files().delete(fileId=idDelete).execute()  # <<<<<here proces file
    gG.archivosProcesados(1,0,0,0)
    if tipo == "text/plain":
        print(f"Archivo borrado totalmente.")
    elif tipo == "application/vnd.google-apps.folder":
        print(f"Folder borrado totalmente.")

def renameCloud(service,idAcces:str,nombreNuevo:str):#renombrea el archivo|folder
    folder_metadata = {
        'name': nombreNuevo
    }
    updateNombre = service.files().update(
        fileId=idAcces,
        body=folder_metadata,
        fields='name'
    ).execute()  # <<<<<here proces file
    gG.archivosProcesados(1,0,0,0)
    print('Renombrado a', updateNombre['name'])

def copiarCloud(service,idA:str,idDe:str,tipo:str)->str:#copia archivo|folder
    if tipo=="text/plain":
        file = service.files().copy(
            fileId=idDe,
            body={
                'parents': [idA]
            }
        ).execute()  # <<<<<here proces file
        gG.archivosProcesados(1,0,0,0)
        print(f"Archivo copiado: {file['name']}")
        return file['id']
    elif tipo == "application/vnd.google-apps.folder":#crear un folder y copiar los archivos
        response = service.files().get(
            fileId=idDe, fields='name, mimeType').execute()#DOBLEX2
        nuevoIdC=crearCloud(service, response["name"], tipo, idA, '')
        resultadoNuevaC = listadoCloud(service, idDe)
        for file in resultadoNuevaC:
            copiarCloud(service, nuevoIdC, file["id"], file["mimeType"])#recursivdiad de otros archivos a copiar
        print(f"Carpeta copiada: {response['name']}")
        return nuevoIdC

def tranferCloud(service,idA:str,idDe:str)->str:
    file = service.files().get(fileId=idDe, fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))
    file = service.files().update(fileId=idDe,
                                  addParents=idA,
                                  removeParents=previous_parents,
                                  fields='id, parents').execute()
    print(f"Directorio movido")
    return file['id']
    
def auxDeParaC(rutaA:str,rutaDE:str)->list[str,str]:#es aux para no copiar mismo codigo de copy.py y tranfer.py

    arrayRuta = gG.arrayRuta(rutaA)
    servicio = servicioCloud()
    resultado = navegacionCarpetasC(
        servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible

    if len(resultado[0]) != 0:  # llegue al final de las carpetas/de
        print(f"La ruta especificada {rutaA}, esta mal")
        return ["", ""]
    idA=resultado[1]["id"]#id rutaA

    arrayRuta = gG.arrayRuta(rutaDE)
    resultado = navegacionCarpetasC(
        servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')

    if len(resultado[0]) != 0:  # llegue al final de las carpetas/de
        print(f"La ruta especificada {rutaDE}, esta mal")
        return ["",""]
    idDe = resultado[1]["id"]  # ida rutaDE
      
    return [idA,idDe]

def escribirCloud(service,idFile,contenidoNeuvo,addMod):
    if addMod=="add":
        contenidoExistente = service.files().get_media(fileId=idFile).execute()#obtengo el contenido nuevo
        # Append new content to the existing content
        contenidoNeuvo = contenidoExistente.decode(
            'utf-8', errors='ignore') + contenidoNeuvo
    media = MediaInMemoryUpload(
        contenidoNeuvo.encode(),
        mimetype='text/plain',
        resumable=True
    )
    service.files().update(
        fileId=idFile,
        media_body=media,
        fields='id, name, mimeType, modifiedTime'
    ).execute()  # <<<<<here proces file
    gG.archivosProcesados(1,0,0,0)
    if addMod == "add":
        print('se agrego al archivo')
    else:
        print('reescrito el archivo')

def upLoading(service,folderLocal,folderCloud):#
    files = os.listdir(folderLocal)#listado del folder
    for file_name in files:
        file_path = os.path.join(folderLocal, file_name)
        if tipo(file_name)=="txt":# subir solo archivos
            # response = service.files().list(
            #    q=f"'{folderCloud}' in parents and name='{file_name}'").execute()
            #f"'{parent_folder_id}' in parents and name='{file_name}'"
            #f"name = '{file_name}'"
            # files = response.get('files', [])
            files=existeNombreC(service,folderCloud,file_name)
            if files["existe"]=="true":#si existe nombre, creo nuevo nombre
                file_name=creRenameC(service,folderCloud,file_name)#nuevo nombre
            file_metadata = {
                'name': file_name,
                'parents': [folderCloud]
                             }
            media = MediaFileUpload(file_path)
            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()  # <<<<<here proces file
            gG.archivosProcesados(1,0,0,0)
            print(f"subiendo archivo {file_name}")
        elif tipo(file_name)=="folder":# crear folder
            resultado = existeNombreC(service, folderCloud, file_name)#existe folder
            if resultado["existe"] == "true":  # si existe nombre, navego en el
                upLoading(service, file_path,resultado["id"])
            else:#si no existe creo nueva carpeta, FIXME: puedo optimzar esta funcion para cuando cree el folder ya no de un listado por que es nueva carpeta
                idFolder=crearCloud(service, file_name,
                           'application/vnd.google-apps.folder',folderCloud,'')
                upLoading(service, file_path, idFolder)


def downLoading(service,folderLocal,folderCloud):
    items = listadoCloud(service,folderCloud)#listado
    for item in items:
        if item['mimeType'] == 'text/plain':  # es un archivo,descargar archivo
            file_name = item['name']
            if os.path.exists(folderLocal+'/'+file_name):  # si existe nombre, creo nuevo nombre
                file_name = creRenameL(folderLocal, file_name)  # nuevo nombre
            request = service.files().get_media(fileId=item['id'])
            with open(folderLocal+'/'+file_name, 'wb') as f:
                f.write(request.execute())
                f.close()
        else:#es un folder,
            #resultado=existeNombreL(folderLocal,item['name'])
            subfolder_path = os.path.join(folderLocal, item['name'])
            os.makedirs(subfolder_path, exist_ok=True)#creo por si no existe
            downLoading(service, subfolder_path, item['id'])
            print(f"Downloaded: {item['name']}")

    print("Download complete!")
    print()