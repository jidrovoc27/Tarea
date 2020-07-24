from grupoModelo import grupModelo
from daoGrupo import Dao
class grupControlador:
    def __init__(self, grup=None):
        self.grupo=grup

    def consulta(self, buscar):
        objDao=Dao()
        return objDao.consultar(buscar)

    def ingresar(self, grup):
        objDao=Dao()
        return objDao.ingresar(grup)

    def modificar(self, grup):
        objDao=Dao()
        return objDao.modificar(grup)

    def eliminar(self, grup):
        objDao=Dao()
        return objDao.eliminar(grup)
