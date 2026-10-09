resumen = "a"
while resumen != "n":
    print("\nMENU")
    print("1. Cargar jugadores")
    print("2. Lista de jugadores")
    print("3. Buscar jugador")
    print("4. Eliminar jugador")
    print("5. Armar parejas")
    print("6. Salir")
    menu = input("Ingrese una opción: ")

    if menu == "1":
        print("\nREGISTRO DE JUGADORES")
        terminar = "s"
        nombres = []
        categorias = []
        while terminar != "n":
            print(f"\nDatos del jugador:")
            nombres.append(input("  Nombre: "))
            categorias.append(input("  Categoría (ej. 4ta, 5ta, 6ta): "))
            terminar = input("¿Desea agregar otro jugador? (s/n): ").lower()
        for i in range(len(nombres)):
            print(nombres[i])
            print(categorias[i])
            with open("inscriptos.txt", "a") as f:
                f.write(f"{nombres[i]} ({categorias[i]})\n")
    elif menu == "2":
        with open("inscriptos.txt", "r") as f:
            lineas = f.readlines()
            for i in lineas:
                print(i.strip())
    elif menu == "3":
        nombre = input("Ingrese el nombre del jugador a buscar: ")
        encontrado = False
        with open("inscriptos.txt", "r") as f:
            lineas = f.readlines()
            for i in lineas:
                if i.startswith(nombre):
                    print("Encontrado:",i.strip()) 
                    encontrado = True
            if encontrado == False:
                print("Jugador no encontrado")
    elif menu == "4":
        nombre = input("Ingrese el nombre del jugador a eliminar: ")
        encontrado = False
        with open("inscriptos.txt", "r") as f:
            lineas = f.readlines()
        for i in lineas:
            if i.startswith(nombre) == False:
                with open("inscriptos.txt", "w") as f:
                    f.write(i)
            if i.startswith(nombre):
                encontrado = True
                print("Jugador eliminado correctamente")
        if encontrado == False:
            print("Jugador no encontrado")
    elif menu == "5":
        jugador1 = input("Ingrese el nombre del primer jugador: ")
        jugador2 = input("Ingrese el nombre del segundo jugador: ")  
        encontrado1 = False
        encontrado2 = False    
        with open("inscriptos.txt", "r") as f:
            lineas = f.readlines()
            for i in lineas:
                if i.startswith(jugador1):
                    jugador1 = i.strip()
                    encontrado1 = True
                if i.startswith(jugador2):
                    encontrado2 = True
                    jugador2 = i.strip()
            with open("parejas.txt", "a") as f:
                f.write(f"Pareja: {jugador1} y {jugador2}\n")
            if encontrado1 and encontrado2 == True:
                print("Pareja creada correctamente con los jugadores:")
                print(jugador1)
                print(jugador2)
            elif encontrado1 == False:
                print("Jugador 1 no encontrado")
            elif encontrado2 == False:
                print("Jugador 2 no encontrado")
    elif menu == "6":
        break
    else:
        print("Opción no válida")
    