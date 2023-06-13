import os
import sys
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG


class Create:
    def __init__(self,):
        self.nombre = ""
        self.contenido = ""
        self.ruta = ""

    def name(self, nombre):
        #posibles cambios necesario al nombre
        if ('"' in nombre):
            self.nombre = nombre.split("\"")[1]
        else:
            self.nombre = nombre

    def body(self, contenido):
        if ('"' in contenido):
            self.contenido = contenido.split("\"")[1]
        else:
            self.contenido = contenido

    def path(self, ruta):
        #posibles cambios necesario ala ruta
        if ('"' in ruta):
            self.ruta = ruta.split("\"")[1]  # FIXME:/"ruta"/->ruta
        else:
            self.ruta = ruta

    def creacionLocal(self):
        #print(self.nombre)
        #print(self.contenido)
        #print(self.ruta)
        pathArchivo = "./archivos"+self.ruta
        if (os.path.exists(pathArchivo+"/"+self.nombre) == True):
            print("Archivo ya existente")
        else:
            if (os.path.exists(pathArchivo) == True):
                #existe la ruta
                # abriendo y creando
                f = open(pathArchivo+"/"+self.nombre, "w")
                f.write(self.contenido)
                f.close()  # siempre cerrar
                print("archivo creado")
            else:
                #si no existe nada
                self.directoriosAnidados(self.ruta)
                f = open(pathArchivo+self.nombre, "w")  # abriendo y creando
                f.write(self.contenido)
                f.close()  # siempre cerrar
                print("ARCHIVO CREADO")

    def directoriosAnidados(self, path):
        split = path.split("/")
        concatenar = "./archivos/"
        for element in split:
            if (element != ""):
                concatenar = concatenar+element+"/"
                if (not (os.path.exists(concatenar))):
                    os.mkdir(concatenar)
                else:
                    print("RUTA YA CREADA")

    def creacionCloud(self):
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
        return


    def creacionCloud(self):
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
        print("se termino de crear todo")
