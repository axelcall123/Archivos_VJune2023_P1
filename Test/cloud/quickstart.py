from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
#CREAR 
    #CARPETA CLOUD
def funcAdFolder(service):
    folder_metadata = {
        'name': 'New Folder123',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(
    body=folder_metadata, fields='id').execute()
    # Retrieve the ID of the newly created folder
    folder_id = folder.get('id')
    print(f'New folder created with ID: {folder_id}')
    #ARCHIVO CLOUD
#ELMINAR EN CLOUD

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
    # Provide the folder name
    nombreFolder = 'New Folder123'
    folder_id = getFolderId(service, nombreFolder)
    if folder_id is None:
        print("Folder not found.")
        exit()
    service.files().delete(fileId=folder_id).execute()
    print(f"Folder '{nombreFolder}' borrado totalmente.")
#COPIAR:
    #CLOUD->CLOUD
#MOVER(TRANSFERIR)
    #CLOUD->CLOUD
    #CLOUD->LOCAL
    #CLOUD->LOCAL
#RENOMBRAR
    #CARPETA CLOUD
    #ARCHIVO CLOUD
#SUSTITUIR
#AGREGARA CONTENIDO

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


#PASO 1:https://www.youtube.com/watch?v=RGXMO8VvmcU
#PASO 2:pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#PASO 3
# If modifying these scopes, delete the file token.json.
scopes=[#
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive'
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
        funcDef(service)
        funcAdFolder(service)
        funcDelFolder(service)
        
        
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'a ocurrido un error: {error}')



if __name__ == '__main__':
    main()
