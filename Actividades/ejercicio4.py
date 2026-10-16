# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 4 – Búsqueda binaria con apellidos
# ==============================================================================
#
# Consigna:
# Leer por teclado 10 apellidos y guardarlos en un vector.
# 1. Programar esta_ordenado(vector), que devuelve True si cada elemento es menor o
#    igual que el siguiente. Si el vector no está ordenado, mostrar:
#    "No se puede usar búsqueda binaria: el vector no está ordenado" y terminar.
# 2. Si está ordenado, leer un apellido y buscarlo con busqueda_binaria(vector, clave).
#    Informar su posición o que no está.
# 3. ¿Qué pasa si se busca "molina", en minúsculas? ¿Cómo lo resolverían?
#
# Para probar:
# Acosta, Benitez, Diaz, Fernandez, Gomez, Ibarra, Lopez, Molina, Ortiz, Romero.
# "Molina" está en la posición 7 y "Perez" no está.
# Con los mismos apellidos en otro orden, el programa tiene que mostrar el aviso del punto 1.
#
# ------------------------------------------------------------------------------
# RESPUESTA AL PUNTO 3:
# ¿Qué pasa si se busca "molina", en minúsculas?
# En Python (según la tabla ASCII / Unicode), todas las letras minúsculas tienen un
# valor numérico mayor que las mayúsculas (por ejemplo, 'm' es 109 y 'Z' es 90).
# Por lo tanto, para Python: "molina" > "Romero".
# Durante la búsqueda binaria, al comparar "molina" con elementos con mayúscula,
# la búsqueda siempre decidirá ir a la derecha y fallará, diciendo que no está.
#
# ¿Cómo lo resolverían?
# Se puede resolver normalizando las cadenas al momento de comparar:
# Usando .lower() en ambos lados (por ejemplo: vector[medio].lower() == clave.lower()),
# o transformando con .capitalize() tanto los apellidos ingresados como la clave de búsqueda.
# ==============================================================================


def esta_ordenado(vector):
    """
    Verifica si cada elemento es menor o igual que el siguiente.
    Retorna True si el vector está ordenado ascendentemente, False en caso contrario.
    """
    for i in range(len(vector) - 1):
        if vector[i] > vector[i + 1]:
            return False
    return True


def busqueda_binaria(vector, clave):
    """
    Realiza la búsqueda binaria de 'clave' en un vector ordenado.
    Retorna la posición donde se encuentra la clave o -1 si no está.
    No utiliza 'in', 'index()' ni 'bisect'.
    """
    inicio = 0
    fin = len(vector) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if vector[medio] == clave:
            return medio
        elif clave > vector[medio]:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

print("=========================================================")
print("      EJERCICIO 4: BÚSQUEDA BINARIA CON APELLIDOS        ")
print("=========================================================")
print("1. Usar lista de prueba ordenada (Acosta, Benitez, ...)")
print("2. Usar lista de prueba DESORDENADA (para verificar control)")
print("3. Ingresar los 10 apellidos manualmente por teclado")

opcion = input("Seleccione una opción (1, 2 o 3): ")

apellidos = []

if opcion == "1":
    apellidos = ["Acosta", "Benitez", "Diaz", "Fernandez", "Gomez", "Ibarra", "Lopez", "Molina", "Ortiz", "Romero"]
    print(f"\nVector cargado: {apellidos}")
elif opcion == "2":
    apellidos = ["Romero", "Acosta", "Gomez", "Diaz", "Benitez", "Ibarra", "Lopez", "Molina", "Ortiz", "Fernandez"]
    print(f"\nVector cargado desordenado: {apellidos}")
else:
    print("\nIngrese 10 apellidos:")
    for i in range(10):
        ap = input(f"Apellido {i + 1}: ").strip()
        apellidos.append(ap)
    print(f"\nVector ingresado: {apellidos}")

# 1. Verificar si está ordenado
if not esta_ordenado(apellidos):
    print("\nNo se puede usar búsqueda binaria: el vector no está ordenado")
else:
    print("\nEl vector está ordenado correctamente. Se procede con la búsqueda binaria.")
    
    # 2. Leer un apellido y buscarlo
    apellido_buscar = input("\nIngrese el apellido a buscar: ").strip()
    
    posicion = busqueda_binaria(apellidos, apellido_buscar)
    
    if posicion != -1:
        print(f"'{apellido_buscar}' está en la posición {posicion}.")
    else:
        print(f"'{apellido_buscar}' no está.")

    # 3. Demostración y explicación de la búsqueda en minúsculas
    print("\n--- EXPLICACIÓN DEL PUNTO 3 (Búsqueda en minúsculas) ---")
    print("¿Qué pasa si se busca 'molina' en minúsculas?")
    pos_min = busqueda_binaria(apellidos, "molina")
    print(f"Resultado directo de buscar 'molina': posición {pos_min} (No lo encuentra).")
    print("Causa: Las letras minúsculas tienen códigos ASCII mayores que las mayúsculas,")
    print("por lo que 'molina' > 'Romero', llevando la búsqueda binaria al extremo derecho.")
    print("Solución: Normalizar las cadenas usando .capitalize() o .lower() antes de comparar.")
