# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 1 – Búsqueda secuencial
# ==============================================================================
#
# Consigna:
# Leer por teclado N números enteros y guardarlos en un vector. Después, leer un número X.
# 1. Con una función busqueda_secuencial(vector, clave), informar la posición de la
#    primera aparición de X, o "X no está en el vector".
# 2. Programar otra función que informe cuántas veces aparece X y en qué posiciones.
#    ¿Por qué esta función no puede cortar el recorrido cuando encuentra a X?
#
# Para probar: con el vector [7, 3, 9, 3, 12, 3, 5], el 3 aparece por primera vez en la
# posición 1 y en total 3 veces (posiciones 1, 3 y 5). El 8 no está.
#
# ------------------------------------------------------------------------------
# RESPUESTA TEÓRICA AL PUNTO 2:
# ¿Por qué esta función no puede cortar el recorrido cuando encuentra a X?
# Respuesta: La función que cuenta y registra todas las posiciones no puede cortar
# porque necesita hacer un recorrido exhaustivo (completo) de todo el vector.
# Si cortara al encontrar la primera coincidencia, ignoraría si el elemento vuelve
# a aparecer más adelante en las posiciones restantes.
# ==============================================================================


def busqueda_secuencial(vector, clave):
    """
    Busca la primera aparición de 'clave' en 'vector'.
    Retorna el índice de la primera aparición o -1 si no se encuentra.
    No utiliza 'in', 'index()' ni 'bisect'.
    """
    posicion = -1
    for i in range(len(vector)):
        if vector[i] == clave:
            posicion = i
            break  # Corta apenas encuentra la primera aparición
    return posicion


def buscar_todas_apariciones(vector, clave):
    """
    Recorre todo el vector para encontrar todas las posiciones donde aparece 'clave'.
    Retorna una lista con los índices encontrados.
    """
    posiciones = []
    for i in range(len(vector)):
        if vector[i] == clave:
            posiciones.append(i)
        # IMPORTANTE: No se usa break porque debe revisar hasta el último elemento
    return posiciones


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

print("==================================================")
print("       EJERCICIO 1: BÚSQUEDA SECUENCIAL           ")
print("==================================================")
print("1. Probar con el ejemplo de la consigna [7, 3, 9, 3, 12, 3, 5]")
print("2. Ingresar datos manualmente por teclado")

opcion = input("Seleccione una opción (1 o 2): ")

vector = []

if opcion == "1":
    vector = [7, 3, 9, 3, 12, 3, 5]
    print(f"\nVector cargado de prueba: {vector}")
else:
    n = int(input("\n¿Cuántos números enteros desea ingresar (N)?: "))
    for i in range(n):
        numero = int(input(f"Ingrese el número para la posición {i}: "))
        vector.append(numero)
    print(f"\nVector cargado: {vector}")

clave_x = int(input("\nIngrese el número X a buscar: "))

# 1. Búsqueda de la primera aparición
pos_primera = busqueda_secuencial(vector, clave_x)

print("\n--- RESULTADO DE LA PRIMERA APARICIÓN ---")
if pos_primera != -1:
    print(f"El número {clave_x} aparece por primera vez en la posición {pos_primera}.")
else:
    print(f"{clave_x} no está en el vector.")

# 2. Búsqueda de todas las apariciones
todas_posiciones = buscar_todas_apariciones(vector, clave_x)
cantidad = len(todas_posiciones)

print("\n--- RESULTADO DE TODAS LAS APARICIONES ---")
if cantidad > 0:
    print(f"El número {clave_x} aparece en total {cantidad} vez/veces.")
    print(f"Posiciones donde aparece: {todas_posiciones}")
else:
    print(f"El número {clave_x} no aparece ninguna vez en el vector.")

print("\n--- PREGUNTA TEÓRICA ---")
print("¿Por qué la función de contar todas las apariciones no puede cortar el recorrido?")
print("Respuesta: Porque debe revisar todo el vector hasta el final. Si cortara al encontrar")
print("la primera coincidencia, no podría saber si el elemento se repite más adelante.")
