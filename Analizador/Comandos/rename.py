import os
class Rename:
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

    




        
            

        
        
    

