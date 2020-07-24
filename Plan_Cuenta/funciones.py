def menu(opciones, titulo):
    print('-'*20)
    print('{}'.format(titulo))
    print('-'*20)
    for op in range(0, len(opciones)):
        print("{}){}".format(op,opciones[op]))
    opc=input('Elija Opcion[0...{}]: '.format(len(opciones)-1))
    return opc

#men=menu(('Grupo de Cuentas','Plan de Cuentas'), 'MENU PRINCIPAL')

