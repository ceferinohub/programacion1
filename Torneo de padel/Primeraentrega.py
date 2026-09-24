cantidadJugadores = int(input("¿Cuántos jugadores van a participar en el torneo? "))

nombres = [""] * cantidadJugadores
categorias = [""] * cantidadJugadores

print("\nREGISTRO DE JUGADORES")
for i in range(cantidadJugadores):
    print(f"\nDatos del jugador {i+1}:")
    nombres[i] = input("  Nombre: ")
    categorias[i] = input("  Categoría (ej. 4ta, 5ta, 6ta): ")

cantidadParejas = cantidadJugadores // 2

if cantidadJugadores % 2 != 0:
    print("\n[Aviso] Se ingresó un número impar. El último jugador quedará sin pareja.")

nombresParejas = [""] * cantidadParejas
jugador1Pareja = [""] * cantidadParejas
jugador2Pareja = [""] * cantidadParejas

print("\nARMADO DE PAREJAS")

print("Jugadores inscriptos disponibles:")
for i in range(cantidadJugadores):
    print(f" {i+1}. {nombres[i]} (Cat: {categorias[i]})")

for i in range(cantidadParejas):
    print(f"\nArmando la pareja {i + 1}:")
    nombresParejas[i] = input("  Nombre de la pareja (ej. 'Los Tanos'): ")
    
    indiceJ1 = int(input("  Ingrese el número del primer jugador: "))
    jugador1Pareja[i] = nombres[indiceJ1-1]
    
    indiceJ2 = int(input("  Ingrese el número del segundo jugador: "))
    jugador2Pareja[i] = nombres[indiceJ2-1]

print("\nRESUMEN DEL TORNEO")
for i in range(cantidadParejas):
    print(f"Pareja '{nombresParejas[i]}': {jugador1Pareja[i]} y {jugador2Pareja[i]}")