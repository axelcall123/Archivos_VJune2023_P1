from datetime import datetime
import tempfile
import os
from Aplicacion.variablesGlobales import temporalFile, encriptado, llaveEncript
from Aplicacion.Analizador import cripto
def arrayRuta(ruta):
    arrayRuta = ruta.split("/")
    for i in range(len(arrayRuta)-1):
        if arrayRuta[i] == '':
            arrayRuta.pop(i)
    return arrayRuta

def bitacora(iO:str,com:str,res:str)->bytes:#input/ouput
    now = datetime.now()
    # tiempo 01/01/01 1: 1: 1
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    strBitacora = f"{dt_string} - {iO} - {com} - Usuario:{res}\n"
    return bytes(strBitacora, 'utf-8')

def existeLogName(path:str,date:str,numero:str)->str:
    if os.path.exists(f'{path}/{date}#{numero}'):  # si existe nombre, creo nuevo nombre
        numeroInt=int(numero)+1
        return existeLogName(path, date, str(numeroInt))
    else:#nuevo nombre creado
        return f'{date}#{numero}'

def closeTempFile():
    global temporalFile
    if temporalFile == None:  # no se creo el archivo, genero uno por si acaso
        temporalFile = tempfile.TemporaryFile()
    # print("efisima", os.path.exists(temporalFile.name), '\n',temporalFile.read().decode("utf-8"))  # existe file temporal
    if temporalFile.read()!=b'':#si existe algo en el archivo creo la carpeta y el log
        path = './archivos/$logs$'
        os.makedirs(path, exist_ok=True)  # creo por si no existe, logs
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y")#formar la carpeta
        path=path+'/'+dt_string
        os.makedirs(path, exist_ok=True)  # creo la subcarpeta log del dia
        nameFile=existeLogName(path,dt_string,'1')
        with open(f'{path}/{nameFile}', 'wb') as f:
            temporalFile.seek(0)  # para leer
            global encriptado, llaveEncript
            if encriptado==True and llaveEncript!="":#encriptar
                arr = bytes(llaveEncript,'utf-8')
                encriptado=cripto.encrypt_string(arr, temporalFile.read().decode("utf-8"))
                f.write(encriptado.hex())
                f.close()
            else:#no encriptar
                f.write(temporalFile.read().decode("utf-8"))
                f.close()
    temporalFile.close()
    #  print("cerrado->", os.path.exists(temporalFile.name))
