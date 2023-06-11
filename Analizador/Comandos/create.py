import os
import sys
import Analizador.Comandos._generalCloud as gC# alias
class Create:
    def __init__ (self,):
        self.nombre=""
        self.contenido=""
        self.ruta=""

    def name (self,nombre):
        #posibles cambios necesario al nombre
        if('"' in nombre):
            self.nombre=nombre.split("\"")[1]
        else:
            self.nombre=nombre
        
        

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.split("\"")[1]
        else:
            self.contenido=contenido


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta

    def creacionLocal(self):
        #print(self.nombre)
        #print(self.contenido)
        #print(self.ruta)
        pathArchivo= "../Archivo/"+self.ruta.split("/")[1]
        #print(pathArchivo)
        if(os.path.exists(pathArchivo+"/"+self.nombre)==True):
            print("Archivo ya existente")
        else:
            if(os.path.exists(pathArchivo)==True):
                #existe la ruta
                f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
                f.write(self.contenido)
                f.close() # siempre cerrar
                print("archivo creado")
            else:
                #si no existe nada
                os.mkdir(pathArchivo)
                f = open(pathArchivo+"/"+self.nombre, "w") #abriendo y creando
                f.write(self.contenido)
                f.close() # siempre cerrar
                print("ARCHIVO CREADO")
    

    
            
    
        
        return
    def creacionCloud(self):
        #print('ver')
        #print(self.nombre, self.contenido, self.ruta)
        arrayRuta=self.ruta.split("/")
        for i in range(len(arrayRuta)-1):
            if arrayRuta[i]=='':
                arrayRuta.pop(i)
        servicio = gC.servicioCloud()
        resultado=gC.navegacionCarpetasC(servicio, arrayRuta,'1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')#navego lo maximo posible
        if len(resultado[0])!=0:#no navego hasta el final de la carpeta, crear carpetas restantes
            res=gC.creacionCarpetaIteraC(servicio, resultado[0], resultado[1]["id"])
            gC.crearCloud(servicio, self.nombre, 'text/plain',res,self.contenido)
        else:#crear archivo
            rename = gC.creRenameC(servicio, resultado[1]["id"], self.nombre)
            gC.crearCloud(servicio, rename,
                          'text/plain', resultado[1]["id"],self.contenido)
        return


        
            

        
        
    
