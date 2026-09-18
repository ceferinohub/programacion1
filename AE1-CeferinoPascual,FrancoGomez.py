opcion = 0
saldo = 50000
while opcion !=4:
    print("\n----------------------------------------------------------------")
    print("1: Consultar saldo disponible")
    print("2: Depositar Dinero(Ingresar un importe)")
    print("3: Extraer Dinero(Restar un importe)")
    print("4: Salir del sistema")
    print("----------------------------------------------------------------\n")
    opcion = int(input("Elige alguna de las opciones anteriores escribiendo el numero de opcion: "))

    if opcion == 1:
        print("\nSu saldo actual es:",saldo)
    else:
        if opcion == 2:
            saldoingresado=float(input("\nIngrese el importe a depositar: $"))
            opcion= input("\nSi se equivoco y quiere volver atras, presione 'a', si quiere confirmar el deposito presione 0: ")
            if opcion=="a":
                print("Operacion cancelada \n")
            else: 
                saldo=saldo+saldoingresado
                print("\nSu nuevo saldo es:",saldo)
                print("\n")
        else:
            if opcion == 3:
                saldoingresado=float(input("\nIngrese el importe a extraer: $"))
                opcion= input("\nSi se equivoco y quiere volver atras, presione 'a', si quiere confirmar la extraccion presione 0: ")
                if opcion=="a":
                    print("\nOperacion cancelada \n")
                else: 
                    if saldo>=saldoingresado:
                        saldo=saldo-saldoingresado
                        print("\nSu nuevo saldo es:",saldo)
                        print("\n")
                    else:
                        print("\nFondos insuficientes para realizar la operación")
                        print("\n")