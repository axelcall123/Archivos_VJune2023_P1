
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
class Backup:
    def __init__ (self,tipo):
        self.tipo=tipo

    def backupA(self):
        folderLocal = './archivos'
        folderCloud = '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm'
        servicio=gC.servicioCloud()
        if self.tipo=="local":#subo a la nuve
            gC.upLoading(servicio,folderLocal,folderCloud)
            print("se suvieron todos los archivos")
        if self.tipo == "cloud":#lo bajo
            gC.downLoading(servicio, folderLocal, folderCloud)
            print("se bajaron todos los archivos")
