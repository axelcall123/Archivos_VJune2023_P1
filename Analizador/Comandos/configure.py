class Configure:
    def __init__ (self,):
        self.logBool=False
        self.readBool=False
        self.local=False
        self.key=""

    def type (self,type):
        if(type.lower()=="local"):
            print("*****SE TRABAJARA LOCALMENTE******")
            self.local=True
            return True
        elif(type.lower()=="cloud"):
            print("*****SE TRABAJARA EN LA NUBE******")
            return False

    def encryptLog(self,logBool):
        if(logBool.lower()=="true"):
            #La bitacora debe de estar encriptada
            self.logBool=True
            return True
        elif(logBool.lower()=="false"):
            #La bitacora NO debe de estar encriptada
            return False
            

    def encryptRead(self,redBool):
        if(redBool.lower()=="true"):
            #el mensaje a leer Esta encriptado
            self.readBool=True
            return True
        elif(redBool.lower()=="false"):
           #el mensaje a leer NO Esta encriptado
            return False
        
    def llave(self,llave):
        #lo que usa la llave
        self.key=llave
        return self.key

    def printConfiguracion(self):
        #Imprimiendo configuraciones del comando
        print(self.local)
        print(self.logBool)
        print(self.readBool)
        print(self.key)

    


        
            

        
        
    

