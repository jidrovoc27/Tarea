from daoCuenta import Dao
from cuentaModelo import cuentModelo

class cuentControlador:
    def __init__(self, cuent=None):
        self.cuenta=cuent

    def consultaCuenta(self, buscar):
        objDao=Dao()
        return objDao.consultarCuenta(buscar)

    def ingresarCuenta(self, cuent):
        objDao=Dao()
        return objDao.ingresarCuenta(cuent)

    def modificarCuenta(self, cuent):
        objDao=Dao()
        return objDao.modificarCuenta(cuent)

    def eliminarCuenta(self, cuent):
        objDao=Dao()
        return objDao.eliminarCuenta(cuent)