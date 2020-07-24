from grupoControlador import grupControlador
from grupoModelo import grupModelo
from cuentaControlador import cuentControlador
from cuentaModelo import cuentModelo
from funciones import menu
import os
grupoControlador=grupControlador()
cuentaControlador=cuentControlador()


def insertar(rango):
    for i in range(int(rango)):
        descripc=input('Ingrese descripcion: ')
        cli=grupModelo(descrip=descripc)
        if grupoControlador.ingresar(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar')

def modificar():
    codigo=input('Ingrese id del dato a modificar: ')
    descripc=input('Ingrese descripción: ')
    cli=grupModelo(cod=codigo, descrip=descripc)
    if grupoControlador.modificar(cli):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar')

def eliminar():
    codigo=input('Ingrese id: ')
    cli=grupModelo(cod=codigo)
    if grupoControlador.eliminar(cli):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar')


def consultar():
    buscar=input('Ingrese nombre a buscar:')
    cli=grupoControlador.consulta(buscar)
    print('Codigo  Descripcion')
    for registro in cli:
        print('{:4}     {:6} '.format(registro[0],registro[1]))

def consultarGrupo():
    buscar=''
    cli=grupoControlador.consulta(buscar)
    print('Codigo  Descripcion')
    for registro in cli:
        print('{:4}     {:6} '.format(registro[0],registro[1]))


#####PLAN DE CUENTAS


def insertarCuenta(rango):
    for i in range(int(rango)):
        codi=input('Ingrese código: ')
        consultar()
        grup=input('Ingrese grupo: ')
        descri=input('Ingrese descripcion: ')
        natura=input('Ingrese naturaleza: ')
        estad=input('Ingrese estado: ')
        cli=cuentModelo(cod=codi, gru=grup, Des=descri, Nat=natura, Est=estad)
        if cuentaControlador.ingresarCuenta(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar')

def modificarCuenta():
    id=input('Ingrese id del dato a modificar: ')
    codigo=input('Ingrese codigo de la cuenta: ')
    consultarGrupo()
    grup=input('Ingrese grupo: ')
    descri=input('Ingrese descripcion: ')
    natura=input('Ingrese naturaleza: ')
    estad=input('Ingrese estado: ')
    cli=cuentModelo(iden=id, cod=codigo, gru=grup, Des=descri, Nat=natura, Est=estad)
    if cuentaControlador.modificarCuenta(cli):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar')

def eliminarCuenta():
    id=input('Ingrese id del dato a eliminar: ')
    cli=cuentModelo(iden=id)
    if cuentaControlador.eliminarCuenta(cli):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar')

def consultarCuenta():
    try:
        buscar=input('Ingrese plan de cuenta a buscar:')
        cli=cuentaControlador.consultaCuenta(buscar)
        print(' Id  Codigo  grupo  Descripcion      Naturaleza    Estado')
        for registro in cli:
            print('{:3}   {:7}{:3}    {:20}{:10} {:3}'.format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5]))
    except Exception as e:
        print('Error', e)


def ejecutar():
    opc=''
    while True:
        opc=str(menu(['Grupo de Cuentas','Plan de Cuentas'],'MENU PRINCIPAL'))
        if opc=='0':
            while True:
                opc=str(menu(['Ingresar','Consultar','Modificar','Eliminar','Retornar Menu Principal'],'MENU GRUPO DE CUENTAS'))
                if opc=='0':
                    print('\n<<<Ingresar>>> ')
                    valor=input('Cantidad de datos a ingresar: ')
                    insertar(valor)

                elif opc=='1':
                    print('\n<<<Consulta de datos')
                    consultar()

                elif opc=='2':
                    print('\n<<<Modificar datos')
                    consultar()
                    modificar()

                elif opc=='3':
                    print('Eliminar datos')
                    consultar()
                    eliminar()

                elif opc=='4':
                    ejecutar()
        elif opc=='1':
            while True:
                opc=str(menu(['Ingresar','Consultar','Modificar','Eliminar','Retornar Menu Principal'],'MENU PLAN DE CUENTAS'))
                if opc=='0':
                    print('\n<<<Ingresar>>> ')
                    valorCuenta=input('Cantidad de datos a ingresar: ')
                    insertarCuenta(valorCuenta)

                elif opc=='1':
                    print('\n<<<Consulta de datos>>> ')
                    consultarCuenta()

                elif opc=='2':
                    print('\n<<<Modificar>>>')
                    consultarCuenta()
                    modificarCuenta()

                elif opc=='3':
                    print('\n<<<Eliminar>>>')
                    consultarCuenta()
                    eliminarCuenta()

                elif opc=='4':
                    ejecutar()

ejecutar()