import sys
from conexion import Conector

class Dao(Conector):
    def __init__(self):
        super().__init__()

    def consultarCuenta(self, buscar):
        result= False
        try:
            sql="Select Id, Codigo, grupo, Descripcion, Naturaleza, Estado from plancuenta where Descripcion like '%" + \
                str(buscar) + "%' order by Id"
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

    def ingresarCuenta(self, cuent):
        correcto=True
        try:
            sql="insert into plancuenta (Codigo, grupo, Descripcion, Naturaleza, Estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,( cuent.cod, cuent.grup, cuent.Des, cuent.Nat, cuent.Est))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificarCuenta(self, cuent):
        correcto=True
        try:
            sql='Update plancuenta set Codigo = %s, grupo=%s, Descripcion=%s, Naturaleza=%s, Estado=%s where Id=%s'
            self.conectar()
            self.conector.execute(sql,(cuent.codigo, cuent.grupo, cuent.descripcion, cuent.naturaleza, cuent.estado,cuent.Id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminarCuenta(self, cuent):
        correcto=True
        try:
            sql='delete from plancuenta where Id= %s'
            self.conectar()
            self.conector.execute(sql, (cuent.Id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


