# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 7 – Pasaje de parámetros
# ==============================================================================
#
# Consigna:
# a) Una función, muchos usos. Escribir una sola vez busqueda_secuencial(vector, clave)
#    y usarla para buscar:
#      - 45 en [12, 45, 7, 30]
#      - "Mendoza" en ["Cordoba", "Rosario", "Mendoza", "Salta"]
#      - "e" en ["p", "a", "d", "e", "l"]
#    Para cada llamada, indicar cuáles son los parámetros formales y cuáles los actuales.
#    Las posiciones esperadas son 1, 2 y 3.
#
# b) ¿Qué imprime? Sin ejecutarlos, escribir qué muestra cada programa.
#    Después, comprobarlo en la computadora y explicar la diferencia.
#
# c) ¿Cómo cambiarían el programa 1 para que numeros no se modifique, y el programa 2
#    para que imprima 1?
#
# ------------------------------------------------------------------------------
# RESPUESTAS TEÓRICAS:
#
# PUNTO A:
# • Parámetros FORMALES: Son las variables declaradas en la definición de la función:
#     def busqueda_secuencial(vector, clave):  -> 'vector' y 'clave'.
# • Parámetros ACTUALES: Son los valores o expresiones concretas enviadas al invocar:
#     - Llamada 1: [12, 45, 7, 30]  y  45
#     - Llamada 2: ["Cordoba", "Rosario", "Mendoza", "Salta"]  y  "Mendoza"
#     - Llamada 3: ["p", "a", "d", "e", "l"]  y  "e"
#
# PUNTO B:
# • Programa 1 imprime:
#     2
#     [10, 20, 30, 40]
#   Explicación: Las listas en Python son objetos MUTABLES que se pasan por referencia.
#   Al hacer 'lista.sort()', se ordena y modifica la lista original 'numeros' en memoria.
#   Luego 'busqueda_binaria' busca el 30 en la lista ya ordenada, encontrándolo en la posición 2.
#
# • Programa 2 imprime:
#     0
#   Explicación: Los números enteros en Python son tipos INMUTABLES. Dentro de la función,
#   'n = n + 1' solo modifica la variable local 'n'. La variable externa 'comparaciones' no se
#   ve afectada. Además, el valor retornado por la función no fue asignado a ninguna variable.
#
# PUNTO C:
# • Para que 'numeros' no se modifique en Programa 1:
#   Se debe trabajar sobre una copia de la lista antes de ordenar:
#     def buscar_ordenando(lista, clave):
#         copia = lista.copy()   # Se hace una copia independiente
#         copia.sort()
#         return busqueda_binaria(copia, clave)
#
# • Para que el Programa 2 imprima 1:
#   Se debe capturar el valor retornado asignándolo nuevamente a la variable:
#     comparaciones = sumar_uno(comparaciones)
#     print(comparaciones)
# ==============================================================================


def busqueda_secuencial(vector, clave):
    """
    Búsqueda secuencial genérica (funciona tanto con enteros como cadenas o caracteres).
    """
    for i in range(len(vector)):
        if vector[i] == clave:
            return i
    return -1


def busqueda_binaria(vector, clave):
    """Búsqueda binaria sobre un vector ordenado."""
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
# PARTE A: UNA FUNCIÓN, MUCHOS USOS
# ==============================================================================
print("=========================================================================")
print("             PARTE A: PARÁMETROS FORMALES Y ACTUALES                     ")
print("=========================================================================")
print("Parámetros formales de la función: (vector, clave)\n")

# Llamada 1
vec1 = [12, 45, 7, 30]
clave1 = 45
pos1 = busqueda_secuencial(vec1, clave1)
print(f"Llamada 1:")
print(f"  Parámetros actuales: vector={vec1}, clave={clave1}")
print(f"  Posición esperada: 1 | Posición obtenida: {pos1}")

# Llamada 2
vec2 = ["Cordoba", "Rosario", "Mendoza", "Salta"]
clave2 = "Mendoza"
pos2 = busqueda_secuencial(vec2, clave2)
print(f"\nLlamada 2:")
print(f"  Parámetros actuales: vector={vec2}, clave='{clave2}'")
print(f"  Posición esperada: 2 | Posición obtenida: {pos2}")

# Llamada 3
vec3 = ["p", "a", "d", "e", "l"]
clave3 = "e"
pos3 = busqueda_secuencial(vec3, clave3)
print(f"\nLlamada 3:")
print(f"  Parámetros actuales: vector={vec3}, clave='{clave3}'")
print(f"  Posición esperada: 3 | Posición obtenida: {pos3}")


# ==============================================================================
# PARTE B: ¿QUÉ IMPRIME? (EJECUCIÓN DE LOS PROGRAMAS ORIGINALES)
# ==============================================================================
print("\n=========================================================================")
print("             PARTE B: COMPORTAMIENTO DE LOS PROGRAMAS                    ")
print("=========================================================================")

# Programa 1 original
def buscar_ordenando_original(lista, clave):
    lista.sort()
    return busqueda_binaria(lista, clave)

numeros_orig = [40, 10, 30, 20]
pos_orig = buscar_ordenando_original(numeros_orig, 30)

print("--- Programa 1 (Original) ---")
print(f"Salida de print(pos):     {pos_orig}")
print(f"Salida de print(numeros): {numeros_orig}")

# Programa 2 original
def sumar_uno(n):
    n = n + 1
    return n

comparaciones_orig = 0
sumar_uno(comparaciones_orig)

print("\n--- Programa 2 (Original) ---")
print(f"Salida de print(comparaciones): {comparaciones_orig}")


# ==============================================================================
# PARTE C: SOLUCIONES MODIFICADAS
# ==============================================================================
print("\n=========================================================================")
print("             PARTE C: VERSIONES CORREGIDAS                               ")
print("=========================================================================")

# Programa 1 modificado: usando .copy() para no alterar la lista original
def buscar_ordenando_sin_modificar(lista, clave):
    copia = lista.copy()
    copia.sort()
    return busqueda_binaria(copia, clave)

numeros_mod = [40, 10, 30, 20]
pos_mod = buscar_ordenando_sin_modificar(numeros_mod, 30)

print("--- Programa 1 Modificado (para que 'numeros' no se altere) ---")
print(f"Posición encontrada en la copia ordenada: {pos_mod}")
print(f"Lista original sin modificar:             {numeros_mod}")

# Programa 2 modificado: asignando el valor retornado
print("\n--- Programa 2 Modificado (para que imprima 1) ---")
comparaciones_mod = 0
comparaciones_mod = sumar_uno(comparaciones_mod)
print(f"Valor de 'comparaciones' luego de asignar el return: {comparaciones_mod}")
