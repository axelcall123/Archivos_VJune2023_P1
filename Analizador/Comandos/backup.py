
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG
class Backup:
    def __init__ (self,tipo):
        self.tipo=tipo

    def backupA(self):
        folderLocal = './Test/cloud/updown_loading'
        folderCloud = '1Cc9Vp0d8EsT2xsWCFMC8Je1rkpFd5TE_'
        servicio=gC.servicioCloud()
        if self.tipo=="local":#subo a la nuve
            gC.upLoading(servicio,folderLocal,folderCloud)
            print("se suvieron todos los archivos")
        if self.tipo == "cloud":#lo bajo
            gC.downLoading(servicio, folderLocal, folderCloud)
            print("se bajaron todos los archivos")
