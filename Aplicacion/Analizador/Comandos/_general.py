from datetime import datetime
import tempfile
import os
from Aplicacion.variablesGlobales import *
from Aplicacion.Analizador import cripto
def arrayRuta(ruta):#pongo split ruta [a,b,c,a.txt]
    arrayRuta = ruta.split("/")
    for i in range(len(arrayRuta)-1):
        if arrayRuta[i] == '':
            arrayRuta.pop(i)
    return arrayRuta

def bitacora(iO:str,com:str,res:str)->bytes:#input/ouput de la bitacora
    now = datetime.now()
    # tiempo 01/01/01 1: 1: 1
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    strBitacora = f"{dt_string} - {iO} - {com} - {res}\n"
    return bytes(strBitacora, 'utf-8')

def existeLogName(path:str,date:str,numero:str)->str:
    if os.path.exists(f'{path}/{date}#{numero}.txt'):  # si existe nombre, creo nuevo nombre
        numeroInt=int(numero)+1
        return existeLogName(path, date, str(numeroInt))
    else:#nuevo nombre creado
        return f'{date}#{numero}'
    
def resetProcesados():
    global tiempoCloud
    global tiempoLocal
    global archivoLocal
    global archivoCloud
    tiempoCloud =0
    tiempoLocal =0
    archivoLocal =0
    archivoCloud =0

def closeTempFile(TF):#cierro y reabro y escribo en el archivo temporal
    global temporalFile
    if temporalFile == None:  # no se creo el archivo, genero uno por si acaso
        temporalFile = tempfile.TemporaryFile()
    # temporalFile.seek(0)
    # print("temporal console", os.path.exists(temporalFile.name), '\n',
    #    temporalFile.read().decode("utf-8"))  # existe file temporal
    temporalFile.seek(0)
    if temporalFile.read().decode("utf-8")!='':  # si existe algo en el archivo creo la carpeta y el log
        path = './archivos/$logs$'
        os.makedirs(path, exist_ok=True)  # creo por si no existe, logs
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y")#formar la carpeta
        path=path+'/'+dt_string
        os.makedirs(path, exist_ok=True)  # creo la subcarpeta log del dia
        nameFile=existeLogName(path,dt_string,'1')
        # with open(f'{path}/{nameFile}.txt', 'wb') as f: solo sirve para bytes
        f = open(f'{path}/{nameFile}.txt', 'w')#solo sirve para str
        temporalFile.seek(0)  # para leer
        global encriptado, llaveEncript
        if encriptado==True and llaveEncript!="":#encriptar
            arr = bytes(llaveEncript.replace("\"",""),'utf-8')
            encriptadoS=cripto.encrypt_string(arr, temporalFile.read().decode("utf-8"))
        
            f.write(str(encriptadoS.hex()))
            f.close()
        else:#no encriptar
            f.write(temporalFile.read().decode("utf-8"))
            f.close()
    temporalFile.close()
    temporalFile=None
    if TF==False:#para cerrarlo totalmente
        temporalFile = tempfile.TemporaryFile()
    #  print("cerrado->", os.path.exists(temporalFile.name))


def escribirTemp(iO: str, com: str, res: str):#me servia solo para ver
    global temporalFile
    # temporalFile.seek(0)
    # print("leer temp<O>\n", temporalFile.read().decode('utf-8'))

    temporalFile.write(bitacora(iO,com,res))
    # temporalFile.seek(0)
    # print("leer temp<N>\n", temporalFile.read().decode('utf-8'))
    
def ecriptadO(encrip,llave):#tengo si se debe encriptar o no ademas de la llave
    global encriptado
    global llaveEncript
    encriptado = encrip
    llaveEncript = llave
    print("")


def cerrrarTemp():#cierro el archivo temporal, para que no quede abierto depues de cerrar totalmente el programa
    global temporalFile
    if temporalFile != None:
        temporalFile.close()
        print("cerrado")

def archivosProcesados(fileCloud:int,fileLocal:int,timeCloud:int,timeLocal:int)->dict:# <<<<<here proces file
    global tiempoCloud
    global tiempoLocal
    global archivoLocal
    global archivoCloud
    tiempoCloud+=timeCloud
    tiempoLocal+=timeLocal
    archivoLocal+=fileLocal
    archivoCloud+=fileCloud
    return {"archivoLocal":archivoLocal,"archivoCloud":archivoCloud,"tiempoLocal":tiempoLocal,"tiempoCloud":tiempoCloud}