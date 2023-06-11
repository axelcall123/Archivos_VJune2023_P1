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

def servicioCloud():
    scopes = [
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive'  # carpeta
    ]
    creds = None
    print("path TF", os.path.exists('token.json'))
    if os.path.exists('token.json'):  # crea un archivo, si no existe con las credenciales
        creds = Credentials.from_authorized_user_file(
            'token.json', scopes)  # leer archivos
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Test\cloud\credentials.json',
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
        return {'existe': "false", "id": idFolderRaiz}
    else:
        for file in files:
            if file['name'] == nombre: 
                return {'existe': "true", "id": file['id']}
            
        return {'existe': "false", "id": idFolderRaiz}

def tipo(nombre:str)->str:
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
        ).execute()
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
                json={"Tipo":"txt","Same":"True","id":json["id"]}
                return [arrayCarpetas,json]
            else:
                print()
        else:#no existe carpeta o archivo
            quetipo = tipo(arrayCarpetas[0])
            if quetipo == "folder":  #llegue al final de mi navegacion en carpetas, [carn,..,txt.txt]|
                json = {"Tipo":"folder","Same": "", "id": json["id"]}
                return [arrayCarpetas, json]
            elif quetipo=="txt":# llegue al final del txt [txt.txt], sin nombre igual
                json = {"Tipo":"txt","Same": "False", "id": json["id"]}
                return [arrayCarpetas, json]
            else:
                print()
    json = {"Tipo": "folder", "Same": "", "id": idFolderRaiz}
    return [arrayCarpetas, json]

def creRenameC(service,idFolderRaiz:str,nombre:str)->str:  # crea el nombre carpeta|archivo que se quiere crear
    resutado=existeNombreC(service, idFolderRaiz, nombre)#FIXME: para no reahacerlo se puede poner otro parametro par unirlo con navacion carpetas
    if resutado["existe"]=="true":#existe nombre
        array=nombre.split(".")
        if len(array)==1:#para folder
            nombre=nombre+'(1)'
        else:#para extension
            nombre=array[0]+'(1).'+array[1]#
        return creRenameC(service, idFolderRaiz,nombre)
    else:#no existe nombre, retorno el nuevo nombre
        return nombre

def creacionCarpetaIteraC(service, array: list[str], idFolder: str) -> str:
    while len(array) != 0:
        idFolder=crearCloud(
            service, array[0], 'application/vnd.google-apps.folder', idFolder, '')
        array.pop(0)
        return creacionCarpetaIteraC(service, array, idFolder)
    return idFolder

def eliminarCloud(service, idDelete:str,tipo):
    service.files().delete(fileId=idDelete).execute()
    if tipo=="txt":
        print(f"Archivo borrado totalmente.")
    elif tipo=="folder":
        print(f"Folder borrado totalmente.")