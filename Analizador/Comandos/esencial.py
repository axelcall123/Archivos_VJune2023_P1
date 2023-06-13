from Analizador.Comandos.create import Create
from Analizador.Comandos.configure import Configure
from Analizador.Comandos.delete import Delete
from Analizador.Comandos.copy import Copy
from Analizador.Comandos.rename import Rename
from Analizador.Comandos.modify import Modify
from Analizador.Comandos.transfer import Transfer
from Analizador.Comandos.exec import Exec
from Analizador.Comandos.add import Add
from Analizador.Comandos.backup import Backup
from Analizador.cripto import encrypt_string, decrypt_string


        #plaintext = "sssssss!"
        #stringK = b'miaproyecto12345'
        #encrypted_data = encrypt_string(stringK, plaintext)
        # Decrypting the string
        #decrypted_data = decrypt_string(stringK, encrypted_data)
        #print("Original String:", plaintext)
        #print("Encrypted Data:", encrypted_data.hex())
        #print("Decrypted String:", decrypted_data)
class Leer:
    def __init__ (self,):
        self.localmente=False
        self.encryptLog=False
        self.encryptRead=False
        self.llave=""

        self.exceString=""

    def comando(self, arreglo):

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
                                    self.localmente = comandoConfigure.type(
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
                            #comandoConfigure.printConfiguracion()
                if (comando == "create" and self.localmente):  # !Comando Create y self.local es True
                    #self.localmente=False
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
                            #comandoCreate.creacionLocal()
                if (comando == "delete" and self.localmente):  # !Comando delete
                    #self.localmente=False
                    comandoDelete = Delete()
                    for parametros in element:
                        if (parametros != "delete"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoDelete.path(elementos2[1])
                                elif (elementos2[0] == "-name->"):
                                    comandoDelete.name(elementos2[1])
                            #borrar
                            #comandoDelete.borrar()
                            #comandoDelete.borrar()
                if (comando == "copy" and self.localmente):  # !Comando delete
                    #self.localmente=False
                    comandoCopy = Copy()
                    for parametros in element:
                        if (parametros != "copy"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    comandoCopy.desde(elementos2[1])
                                elif (elementos2[0] == "-to->"):
                                    comandoCopy.to(elementos2[1])
                            #copiar
                            #comandoCopy.copiar()
                            #comandoCopy.copiarCloud()
                if (comando == "transfer" and self.localmente):  # !Comando trasnfer
                    #self.localmente=False
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
                            #transferir
                            #comandoTransfer.transferir()
                            #comandoTransfer.transferir()
                if (comando == "rename" and self.localmente):  # !Comando rename
                    #self.localmente=False
                    comandoRenombrar = Rename()
                    for parametros in element:
                        if (parametros != "rename"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoRenombrar.path(elementos2[1])
                                elif (elementos2[0] == "-name->"):
                                    comandoRenombrar.name(elementos2[1])
                            #renombrar
                            #comandoRenombrar.reNombrar()
                            #comandoRenombrar.renameCloud()
                if (comando == "modify" and self.localmente):  # !Comando modify
                    #self.localmente=False
                    comandoModificar = Modify()
                    for parametros in element:
                        if (parametros != "modify"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoModificar.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoModificar.body(elementos2[1])
                            #modificar
                            #comandoModificar.modificar()
                            comandoModificar.modificarCloud()
                if (comando == "add" and self.localmente):  # !Comando add
                    #self.localmente=False
                    comandoAgregar = Add()
                    for parametros in element:
                        if (parametros != "add"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoAgregar.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoAgregar.body(elementos2[1])
                            #añadir
                            comandoAgregar.aniadir()
                if (comando == "exec" and self.localmente):  # !Comando add
                    #self.localmente=False

                    comandoEjecutar = Exec()
                    for parametros in element:
                        if (parametros != "exec"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoEjecutar.path(elementos2[1])
                            #añadir
                            ##comandoAgregar.aniadir()
                            #comandoAgregar.agregarCloud()
                            self.exceString = comandoEjecutar.ejecutarArchivo()
                            return self.exceString
                    if (comando == "backup" and self.localmente):  # !Comando add
                        comandoBackup = Backup("local")
                        comandoBackup.backupA()
                   


