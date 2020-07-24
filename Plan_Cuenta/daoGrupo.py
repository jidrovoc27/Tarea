import sys
from conexion import Conector

class Dao(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result= False
        try:
            sql="Select id, descripcion from grupo where descripcion like '%" + \
                str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, grup):
        correcto=True
        try:
            sql="insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql,grup.descripcion)
            self.conn.commit()
        except Exception as e:
            print("Error al insertar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, grup):
        correcto=True
        try:
            sql='Update grupo set descripcion = %s where id=%s'
            self.conectar()
            self.conector.execute(sql,(grup.descripcion, grup.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, grup):
        correcto=True
        try:
            sql='delete from grupo where id= %s'
            self.conectar()
            self.conector.execute(sql, (grup.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto