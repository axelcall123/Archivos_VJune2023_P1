import os
import shutil

class Transfer:
    def __init__ (self,):
        self.de=""
        self.a=""
        self.modo=""

    def desde (self,de):
        if('"' in de):
            self.de=de.split("\"")[1]
        else:
            self.de=de

    def to(self,a):
        if('"' in a):
            self.a=a.split("\"")[1]
        else:
            self.a=a

    def mode(self,mode):
        if('"' in mode):
            self.modo=mode.split("\"")[1]
        else:
            self.modo=mode

    
       
            
