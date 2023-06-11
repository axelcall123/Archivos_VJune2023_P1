import os
class Modify:
    def __init__ (self,):
        self.contenido=""
        self.ruta=""

    def body (self,contenido):
        self.contenido=contenido
            

    def path(self,ruta):
        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta

    
        




        
            

        
        
    

