import os
class Delete:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

    def path (self,ruta):

        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta

    def name(self,nombre):
        if('"' in nombre):
            self.nombre="/"+nombre.split("\"")[1]+"/"
        else:
            self.nombre=nombre

    def borrar(self):
        pathArchivo= "../Archivo/"+self.ruta.split("/")[1]
        print(pathArchivo)
        
        if(os.path.exists(pathArchivo+"/"+self.nombre)&(self.nombre!="")):
            os.remove(pathArchivo+"/"+self.nombre)
            print("******EL ARCHIVO FUE BORRADO CON EXITO******")
            
        else:
            if(os.path.exists(pathArchivo)==True):
                #existe la ruta
                #print("--------------------------------------------------------------"+pathArchivo+"/"+self.nombre)
                print(pathArchivo)
                os.rmdir(pathArchivo)
                print("******LA CARPETA FUE BORRADO CON EXITO******")
            else:
                #si no existe nada
                 print("******ERROR NO SE ENCONTRO LA DIRECCIOn******")
            





        
            

        
        
    

