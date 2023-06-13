import os
class Add:
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

    def aniadir(self):
        pathArchivo= "./archivos"+self.ruta
        if(os.path.exists(pathArchivo)):
            f = open(pathArchivo, "a+") #abriendo y creando
            f.write(f.read()+self.contenido)
            f.close() # siempre cerrar
            print("******SE AÑADIO CONTENIDO AL ARCHIVO CON EXITO******")
            
        else:
             print("******ERROR NO SE ENCONTRO LA DIRECCION ******")
        




        
            

        
        
    

