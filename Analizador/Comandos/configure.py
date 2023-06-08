class Configure:
    def __init__ (self,):
        pass


    def type (self,typeBool):
        if(typeBool.lower()=="local"):
            self.local=True
            return True
        elif(typeBool.lower()=="cloud"):
            return False

    def encryptLog(self,logBool):
        if(logBool.lower()=="true"):
            #mandar a encriptar
            pass
        elif(logBool.lower()=="false"):
            #mensaje no se encripta
            pass

    def encryptRead(self,redBool):
        if(redBool.lower()=="true"):
            #el mensaje esta encriptado
            pass
        elif(redBool.lower()=="false"):
            #el mensaje NO esta encriptado
            pass
        
    def llave(self,llave):
        #lo que usa la llave
        pass



        
            

        
        
    
a=Configure()
a.type("local")