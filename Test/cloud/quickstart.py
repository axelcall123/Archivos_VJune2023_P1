from __future__ import print_function

import os.path
import time
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaInMemoryUpload
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload

#CREAR 
#->CARPETA CLOUD
def funcAdFolder(service):
    parent_folder_id = '1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_'
    new_folder_name = 'FOLDER FUNC'
    folder_metadata = {
        'name': new_folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]
    }
    folder = service.files().create(
    body=folder_metadata, fields='id').execute()
    # Retrieve the ID of the newly created folder
    #folder_id = folder.get("id")
    print(f'New folder created with ID: {folder.get("id")}')

#->ARCHIVO CLOUD
def funcAdFile(service):
    file_name = 'example.txt'
    parent_folder_id = '1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_'
    file_content = 'This is the content of the file.'
    file_metadata = {
        'name': file_name,
        'mimeType': 'text/plain',
        'parents': [parent_folder_id]
    }
    media = MediaInMemoryUpload(
        file_content.encode(),
        mimetype='text/plain',
        resumable=True
    )
    created_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(f'File created with ID: {created_file.get("id")}')

#ELIMINAR EN CLOUD
#->CARPETA
def getFolderId(service,folder_name):
    response = service.files().list(
        q="mimeType='application/vnd.google-apps.folder' and trashed=false",
        spaces='drive',
        fields='files(id, name)',
    ).execute()

    folders = response.get('files', [])
    for folder in folders:
        if folder['name'] == folder_name:
            return folder['id']
    return None

def funcDelFolder(service):
    start_time = time.time()#inicio 
    # Provide the folder name
    nombreFolder = 'Newa Folder123s'
    folder_id = getFolderId(service, nombreFolder)
    if folder_id is None:
        print("Folder not found.")
        exit()
    service.files().delete(fileId=folder_id).execute()
    print(f"Folder '{nombreFolder}' borrado totalmente.")
    end_time = time.time()
    print((end_time - start_time) * 1000, "ms tardo la accion")
#->ARCHIVO
def getFileId(service, file_name):
    response = service.files().list(
        q="mimeType='text/plain' and trashed=false",
        spaces='drive',
        fields='files(id, name)',
    ).execute()

    folders = response.get('files', [])
    print(f'folders {folders}')
    for folder in folders:
        if folder['name'] == file_name:
            return folder['id']
    return None

def funcDelFile(service):
    nombreFile = 'txt.txt'
    folder_id = getFileId(service, nombreFile)
    if folder_id is None:
        print("File not found.")
        exit()
    service.files().delete(fileId=folder_id).execute()
    print(f"File '{nombreFile}' borrado totalmente.")
#COPIAR:
#->CLOUD->CLOUD
def copiarA(service):
    file_id = '1A96eWVdigi-6NFAD9A4igr1n_fnXkH94'
    #1lp5hpiseOF8ZwLeZmUMKeeEwGTXtkk-5 txt D2
    #1A96eWVdigi-6NFAD9A4igr1n_fnXkH94 folder
    new_folder_id = '1FsK1SNHhUmSZxiLDyb2-Au3oVrLWwMqC'
    file = service.files().copy(
        fileId=file_id,
        body={
            'parents': [new_folder_id]
        }
    ).execute()
    print(f"File copied successfully: {file['name']}")
def copiarF(service):
    source_folder_id = '1A96eWVdigi-6NFAD9A4igr1n_fnXkH94'#id
    # Retrieve the metadata of the source folder
    source_folder = service.files().get(fileId=source_folder_id).execute()
    # Create a copy of the source folder
    destination_folder_id = '1FsK1SNHhUmSZxiLDyb2-Au3oVrLWwMqC'
    copied_folder = {
        'name': source_folder['name'],
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [destination_folder_id]
    }

    new_folder_id = '1FsK1SNHhUmSZxiLDyb2-Au3oVrLWwMqC'
    new_folder = service.files().copy(fileId=new_folder_id,
                                      body=copied_folder).execute()
    # Recursively copy the contents of the source folder
    print('Folder copied successfully!')
#MOVER(TRANSFERIR)
#->CLOUD->CLOUD
def moverCC(service):
    directory_id = '1HVmSG9e677YTy_LghQjDzf7wc3RftAY2'  # D2 to
    new_parent_id = '1yLewbtwvm2mhjy0Qy2hXplYAzvXzxPBv'  # D1
    file = service.files().get(fileId=directory_id, fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))
    file = service.files().update(fileId=directory_id,
                                  addParents=new_parent_id,
                                  removeParents=previous_parents,
                                  fields='id, parents').execute()
    print(f"Directory moved. New ID: {file['id']}")
#->CLOUD->LOCAL
def downlaod(service):#arbol para descargar carpetas
    file_id = "1-HbFkMf6Vx_r2S_zJg0u0caBJ0BmULbZ"
    #1-HbFkMf6Vx_r2S_zJg0u0caBJ0BmULbZ txt
    #1sdYArWvhLydeLo-6CPcedMF6Jdpep6Ghv6H8LnREHdU docs
    destination_folder = "D:/AXEL/DOCUMENTOS/U--OTROS/GITHUB/ARCHIVOS/VACAS#1_2023/Archivos_VJune2023_P1/Test/cloud/file"
    # Request the file metadata
    file = service.files().get(fileId=file_id).execute()
    # Get the file name and extension
    file_name = file['name']
    #file_extension = os.path.splitext(file_name)[1]
    # Set the destination file path
    destination_file_path = os.path.join(destination_folder, file_name)
    # Download the file
    request = service.files().get_media(fileId=file_id)
    fh = open(destination_file_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download progress: {int(status.progress() * 100)}%")
    fh.close()
    
    print("File downloaded successfully.")
#->LOCAL->CLOUD
def moverLCA(service):
    file_path = 'D:/AXEL/DOCUMENTOS/U--OTROS/GITHUB/ARCHIVOS/VACAS#1_2023/Archivos_VJune2023_P1/Test/cloud/file/local.txt'
    folder_id = '1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_'
    file_metadata = {
        'name': 'file.txt',
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, mimetype='application/octet-stream')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % file.get('id'))

def moverLCF(service):
    folder_path = 'D:/AXEL/DOCUMENTOS/U--OTROS/GITHUB/ARCHIVOS/VACAS#1_2023/Archivos_VJune2023_P1/Test/cloud/updown_loading'
    # List files in the local folder
    folder_id = '1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_'
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Upload file to Google Drive
            file_metadata = {
                'name': file_name,
                'parents': [folder_id]
                             }
            media = MediaFileUpload(file_path)
            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
#RENOMBRAR
def renameC(service):
    # ID of the folder to rename
    folder_id = '12c9bVxeYdTVr88yNHgstHeNkvnadQf1o'
    #14mf-71FoRsZqhPqRCQnWEZxgUJPnrArw folder D
    #12c9bVxeYdTVr88yNHgstHeNkvnadQf1o txt
    # New name for the folder
    new_name = 'local.txt'
    # Update the folder's name
    folder_metadata = {
        'name': new_name
    }
    updated_folder = service.files().update(
        fileId=folder_id,
        body=folder_metadata,
        fields='name'
    ).execute()
    # Print the updated folder's name
    print('Folder renamed to:', updated_folder['name'])
#SUSTITUIR
def sust(service):
    #buscar txt
    # file_name = 'local.txt'
    # query = f"name='{file_name}'"
    # response = service.files().list(q=query).execute()
    # files = response.get('files', [])
    # if files:
    #    file_id = files[0]['id']
    file_id = '12c9bVxeYdTVr88yNHgstHeNkvnadQf1o'
    new_content = "This is the new content of the file."

    media = MediaInMemoryUpload(
        new_content.encode(),
        mimetype='text/plain',
        resumable=True
    )
    service.files().update(
        fileId=file_id,
        media_body=media,
        fields='id, name, mimeType, modifiedTime'
    ).execute()
    print('reescrito')
    #     print("File content updated successfully.")
    # else:
    #     print("File not found.")
#AGREGARA CONTENIDO
def agregar(service):
    # Read the existing content of the file
    file_id = '12c9bVxeYdTVr88yNHgstHeNkvnadQf1o'
    content='\nnuevo contenido perron'
    existing_content = service.files().get_media(fileId=file_id).execute()
    # Append new content to the existing content
    new_content = existing_content.decode('utf-8', errors='ignore') + content
    # Update the file with the new content
    media = MediaInMemoryUpload(
        new_content.encode(),
        mimetype='text/plain',
        resumable=True
    )
    service.files().update(
        fileId=file_id,
        media_body=media,
        fields='id, name, mimeType, modifiedTime'
    ).execute()
    print('Content added successfully!')
#NAVEGACION
def tipo(nombre):
    arr=nombre.split(".")
    if len(arr) == 1:
        return "folder"
    elif len(arr) == 2:
        return arr[1]

def getContentC(service):
    folder_id = '1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_'
    #1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_ TEST
    #1A96eWVdigi-6NFAD9A4igr1n_fnXkH94 A
    # Retrieve the contents of the specified folder
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name, mimeType)").execute()
    files = results.get('files', [])
    if not files:
        print('No files found.')
    else:
        print('Files in the folder:')
        for file in files:
            print(f"Name: {file['name']}, ID: {file['id']}, Type: {file['mimeType']}")

def getContentL():
    ejemplo_dir = 'Test/cloud/TEST/A'
    # with os.scandir(ejemplo_dir) as ficheros:
    #     for fichero in ficheros:
    #         print(fichero.name, tipo(fichero.name))
    dir = os.listdir(ejemplo_dir)
    # Checking if the list is empty or not
    if len(dir) == 0:
        print("No files found")
    else:
        for fichero in dir:
            print(fichero, tipo(fichero))
        

#DEFAULT
def funcDef(service):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # Call the Drive v3 API, buscar 10 archivos por id y nombre
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
        return
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))
    #end func
    print()



def Test():
    jsonT = {'A': 'a', "B": "b"}
    print(jsonT,jsonT['A'])
#PASO 1:https://www.youtube.com/watch?v=RGXMO8VvmcU
#PASO 2:pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#PASO 3
# If modifying these scopes, delete the file token.json.
scopes=[#
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive'#carpeta
    #'https://www.googleapis.com/auth/drive.file'#archivos
]
#enlace que podes hacer, credenciales para modificar etcc...
#abilitar api json, drive

def main():
    creds = None
    print("path TF", os.path.exists('token.json'))
    if os.path.exists('token.json'):  # crea un archivo, si no existe con las credenciales
        creds = Credentials.from_authorized_user_file(
             'token.json', scopes)  # leer archivos
        #FIXME:solo una vez puede ser llamado
        # creds = service_account.Credentials.from_service_account_file(
        #     'path/to/service_account_credentials.json',
        #     scopes[1]
        #     )  # crear carpetas

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Test/cloud/credentials.json',
                scopes)  # se le entrega todos las credenciales
            creds = flow.run_local_server(port=0)

        # guarda las credenciales par el siguiente arranque
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # acceso a la nube,buscar,subir
        service = build('drive', 'v3', credentials=creds)
        #funcDef(service)
        #funcAdFolder(service)
        #funcDelFolder(service)
        #funcAdFile(service)
        #funcDelFile(service)
        #moverCC(service)
        #downlaod(service)
        #copiarA(service)
        #moverLCF(service)
        moverLCF(service)
        #renameC(service)
        #sust(service)
        #agregar(service)
        #getContentL()
        #print("---")
        #getContentC(service)
        Test()
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'a ocurrido un error: {error}')



if __name__ == '__main__':
    main()
