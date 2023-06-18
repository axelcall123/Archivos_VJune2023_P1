import os
import sys
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
class Create:
    def __init__ (self,):
        self.nombre=""
        self.contenido=""
        self.ruta=""

    def name (self,nombre):
        #posibles cambios necesario al nombre
        if('"' in nombre):
            self.nombre=nombre.replace("\"", "" )
        else:
            self.nombre=nombre
        
        

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.replace("\"", "" )
        else:
            self.contenido=contenido


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta

    def creacionLocal(self):
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'create', f'path:{self.ruta} name:{self.nombre} | local')
        #print(self.nombre)
        #print(self.contenido)
        #print(self.ruta)
        pathArchivo= "./archivos/"+self.ruta
        #verificando Ya exista ruta y archivo
        if(os.path.exists(pathArchivo+"/"+self.nombre)):

            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'create', 'archivo ya existe')
            print("Archivo ya existente")
        #si hay ruta pero no archivo
        else:
            if(os.path.exists(pathArchivo)):
                #existe la ruta
                f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
                f.write(self.contenido)  # <<<<<here proces file
                gG.archivosProcesados(0, 1, 0, 0)
                f.close() # siempre cerrar
                print("archivo creado")
            else:
                #si no existe nada
                self.directoriosAnidados(self.ruta)
                f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
                f.write(self.contenido)  # <<<<<here proces file
                gG.archivosProcesados(0, 1, 0, 0)
                f.close() # siempre cerrar
                print("ARCHIVO CREADO")
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'create', 'fueron los archivos creados')

    def directoriosAnidados(self,path):
        split=path.split("/")
        concatenar="./archivos/"
        for element in split:
            if(element!=""):
                concatenar=concatenar+element+"/"
                if(not(os.path.exists(concatenar))):
                    os.mkdir(concatenar) 
                else:
                    print("RUTA YA CREADA")
                    
    def creacionCloud(self):
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'input', 'create', f'path:{self.ruta} name:{self.nombre} | cloud')
        #print('ver')
        #print(self.nombre, self.contenido, self.ruta)
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        # no navego hasta el final de la carpeta, crear carpetas restantes
        if len(resultado[0]) != 0:
            res = gC.creacionCarpetaIteraC(
                servicio, resultado[0], resultado[1]["id"])
            gC.crearCloud(servicio, self.nombre,
                          'text/plain', res, self.contenido)
        else:  # crear archivo
            rename = gC.creRenameC(servicio, resultado[1]["id"], self.nombre)
            gC.crearCloud(servicio, rename,
                          'text/plain', resultado[1]["id"], self.contenido)
        #bitacora<<<<>>>>>
        gG.escribirTemp(
            'output', 'create', 'fueron los archivos creados')
        print("se termino de crear todo")