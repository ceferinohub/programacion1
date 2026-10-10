archivoSaldo = "saldo.txt"
archivoMovimientos = "movimientos.txt"

def cargarSaldo():
    with open(archivoSaldo, "r") as f:
        contenido = f.read().strip()
        if contenido != "":
            return float(contenido)
        else:
            saldoInicial = 50000.0
            guardarSaldo(saldoInicial)
            return saldoInicial


def guardarSaldo(saldo):
    with open(archivoSaldo, "w") as f:
        f.write(f"{saldo}")


def registrarMovimiento(tipo, importe, saldoResultante):
    linea = f"${importe} Saldo restante: ${saldoResultante}\n"
    with open(archivoMovimientos, "a") as f:
        f.write(linea)


def verHistorialMovimientos():
    print("\nHISTORIAL DE MOVIMIENTOS")
    with open(archivoMovimientos, "r") as f:
        lineas = f.readlines()
        if not lineas:
            print("El archivo de movimientos está vacío.")
        else:
            for i in lineas:
                print(i.strip())

saldo = cargarSaldo()
opcion = 0

while opcion != 5:
    print("\n1: Consultar saldo disponible")
    print("2: Depositar Dinero")
    print("3: Extraer Dinero")
    print("4: Ver historial de movimientos")
    print("5: Salir del sistema")
    opcion = int(input("\nElige alguna de las opciones anteriores escribiendo el número de opción: "))

    if opcion == 1:
        print(f"\nSu saldo actual es: ${saldo}")

    elif opcion == 2:
        saldoingresado = float(input("\nIngrese el importe a depositar: $"))
        if saldoingresado <= 0:
            print("El importe a depositar debe ser mayor a 0.")
        else:
            confirmacion = input("\nSi se equivocó y quiere volver atrás presione 'a', para confirmar presione '0': ").lower()
            if confirmacion == "a":
                print("Operación cancelada\n")
            elif confirmacion == "0":
                saldo = saldo + saldoingresado
                guardarSaldo(saldo)
                registrarMovimiento("Depósito", saldoingresado, saldo)
                print(f"\nDepósito exitoso. Su nuevo saldo es: ${saldo}\n")
            else:
                print("Opción de confirmación no válida. Operación cancelada.\n")

    elif opcion == 3:
        saldoingresado = float(input("\nIngrese el importe a extraer: $"))
        if saldoingresado <= 0:
            print("El importe a extraer debe ser mayor a 0.")
        confirmacion = input("\nSi se equivocó y quiere volver atrás presione 'a', para confirmar presione '0': ").lower()
        if confirmacion == "a":
            print("\nOperación cancelada\n")
        elif confirmacion == "0":
            if saldo >= saldoingresado:
                saldo = saldo - saldoingresado
                guardarSaldo(saldo)
                registrarMovimiento("Extracción", saldoingresado, saldo)
                print(f"\nExtracción exitosa. Su nuevo saldo es: ${saldo}\n")
            else:
                print("\nFondos insuficientes para realizar la operación\n")
        else:
            print("Opción de confirmación no válida. Operación cancelada.\n")

    elif opcion == 4:
        verHistorialMovimientos()
    elif opcion == 5:
        break
    else:
        print("\nOpción no válida. Por favor seleccione un número del 1 al 5.")
