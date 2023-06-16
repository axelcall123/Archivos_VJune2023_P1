
from Aplicacion.Analizador.Comandos.create import Create
from Aplicacion.Analizador.Comandos.configure import Configure
from Aplicacion.Analizador.Comandos.delete import Delete
from Aplicacion.Analizador.Comandos.copy import Copy
from Aplicacion.Analizador.Comandos.rename import Rename
from Aplicacion.Analizador.Comandos.modify import Modify
from Aplicacion.Analizador.Comandos.transfer import Transfer
from Aplicacion.Analizador.Comandos.exec import Exec
from Aplicacion.Analizador.Comandos.add import Add
#from Aplicacion.Analizador.cripto import encrypt_string,decrypt_string
#from Aplicacion.variablesGlobales import localmente
from Aplicacion.Analizador.Comandos.backup import Backup
#import tempfile
import Aplicacion.Analizador.Comandos._general as gG
from Aplicacion.variablesGlobales import encriptado, llaveEncript,local

        #plaintext = "sssssss!"
        #stringK = b'miaproyecto12345'
        #encrypted_data = encrypt_string(stringK, plaintext)
        # Decrypting the string
        #decrypted_data = decrypt_string(stringK, encrypted_data)
        #print("Original String:", plaintext)
        #print("Encrypted Data:", encrypted_data.hex())
        #print("Decrypted String:", decrypted_data) 

class Leer:
    def __init__(self,):
        self.encryptLog = False
        self.encryptRead = False
        self.llave = ""

        self.exceString = ""

    def comando(self, arreglo):
        print("------------------------------")

        #la cantidad de comandos
        #print(arreglo)
        for element in arreglo:
            # cuales comandos
            for comando in element:
                # Separando comandos
                if (comando == "configure"):  # !Comando Configure
                    comandoConfigure = Configure()
                    for parametros in element:
                        if (parametros != "configure"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type->"):
                                    global local
                                    local = comandoConfigure.type(
                                        elementos2[1])
                                elif (elementos2[0] == "-encrypt_log->"):
                                    self.encryptLog = comandoConfigure.encryptLog(
                                        elementos2[1])
                                elif (elementos2[0] == "-encrypt_read->"):
                                    self.encryptRead = comandoConfigure.encryptRead(
                                        elementos2[1])
                                elif (elementos2[0] == "-llave->"):
                                    self.llave = comandoConfigure.llave(
                                        elementos2[1])
                            #print configure
                            #bitacora<<<<>>>>>
                            gG.escribirTemp(
                                'input', 'configure', comandoConfigure.printConfiguracion())
                            gG.ecriptadO(comandoConfigure.encryptLog,
                                         comandoConfigure.llave)
                if (comando == "create"):  # !Comando Create y self.local es True
                    #local=False
                    comandoCreate = Create()
                    for parametros in element:
                        if (parametros != "create"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-name->"):
                                    comandoCreate.name(elementos2[1])
                                elif (elementos2[0] == "-path->"):
                                    comandoCreate.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoCreate.body(elementos2[1])
                            #creando archivo
                            if (local == True):
                                comandoCreate.creacionLocal()
                            else:
                                comandoCreate.creacionCloud()
                if (comando == "delete"):  # !Comando delete
                    #local=False
                    comandoDelete = Delete()
                    for parametros in element:
                        if (parametros != "delete"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoDelete.path(elementos2[1])
                                elif (elementos2[0] == "-name->"):
                                    comandoDelete.name(elementos2[1])
                            #! Dependiento del configure
                            if (local == True):
                                comandoDelete.borrar()
                            else:
                                comandoDelete.borrarCloud()
                if (comando == "copy"):  # !Comando delete
                    #local=False
                    comandoCopy = Copy()
                    for parametros in element:
                        if (parametros != "copy"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    comandoCopy.desde(elementos2[1])
                                elif (elementos2[0] == "-to->"):
                                    comandoCopy.to(elementos2[1])
                            #! Dependiento del configure
                            if (local == True):
                                comandoCopy.copiar()
                            else:
                                comandoCopy.copiarCloud()
                if (comando == "transfer"):  # !Comando trasnfer
                    #local=False
                    comandoTransfer = Transfer()
                    for parametros in element:
                        if (parametros != "transfer"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    comandoTransfer.desde(elementos2[1])
                                elif (elementos2[0] == "-to->"):
                                    comandoTransfer.to(elementos2[1])
                                elif (elementos2[0] == "-mode->"):
                                    comandoTransfer.mode(elementos2[1])
                            #! Dependiento del configure
                            if (local == True):
                                comandoTransfer.transferir()
                            else:
                                comandoTransfer.transferCloud()
                if (comando == "rename"):  # !Comando rename
                    #local=False
                    comandoRenombrar = Rename()
                    for parametros in element:
                        if (parametros != "rename"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoRenombrar.path(elementos2[1])
                                elif (elementos2[0] == "-name->"):
                                    comandoRenombrar.name(elementos2[1])
                            #! Dependiento del configure
                            if (local == True):
                                comandoRenombrar.reNombrar()
                            else:
                                comandoRenombrar.renameCloud()
                if (comando == "modify"):  # !Comando modify
                    #local=False
                    comandoModificar = Modify()
                    for parametros in element:
                        if (parametros != "modify"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoModificar.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoModificar.body(elementos2[1])
                            #! Dependiento del configure
                            if local == True:
                                comandoModificar.modificar()
                            else:
                                comandoModificar.modificarCloud()
                if (comando == "add"):  # !Comando add
                    #local=False
                    comandoAgregar = Add()
                    for parametros in element:
                        if (parametros != "add"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoAgregar.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoAgregar.body(elementos2[1])
                            #añadir
                            if local == True:
                                comandoAgregar.aniadir()
                            else:
                                comandoAgregar.agregarCloud()
                if (comando == "exec"):  # !Comando exec
                    #local=False
                    comandoEjecutar = Exec()
                    for parametros in element:
                        if (parametros != "exec"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoEjecutar.path(elementos2[1])
                            self.exceString = comandoEjecutar.ejecutarArchivo()
                            #print(self.exceString)
                            return self.exceString
                if (comando == "backup"):  # !Comando 
                    comandoBackup = None
                    #! Dependiento del configure 
                    if local == True:
                        comandoBackup = Backup("local")
                    else:
                        comandoBackup = Backup("cloud")
                    comandoBackup.backupA()
                if (comando == "error"):  # !Comando add
                    print("ERROR GRAMATICA")
        