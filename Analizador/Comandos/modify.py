import os
class Modify:
    def __init__ (self,):
        self.contenido=""
        self.ruta=""

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.split("\"")[1]
        else:
            self.contenido=contenido
            

    def path(self,ruta):
        if('"' in ruta):
            self.ruta=ruta.split("\"")[1]
        else:
            self.ruta=ruta

    def modificar(self):
        pathArchivo= "./Archivo"+self.ruta
        print(pathArchivo)
        
        if(os.path.exists(pathArchivo)):
            f = open(pathArchivo, "w") #abriendo y creando
            f.write(self.contenido)
            f.close() # siempre cerrar
            print("******EL ARCHIVO FUE MODIFICADO CON EXITO******")
            
        else:
             print("******ERROR NO SE ENCONTRO LA DIRECCION******")
        




        
            

        
        
    

