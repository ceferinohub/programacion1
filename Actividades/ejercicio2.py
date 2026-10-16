# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 2 – Secuencial con corte en un vector ordenado
# ==============================================================================
#
# Consigna:
# Si el vector está ordenado de menor a mayor, la búsqueda secuencial puede terminar
# apenas encuentra un elemento mayor que la clave, porque de ahí en adelante sólo hay
# valores mayores.
#
# 1. Programar secuencial_con_corte(vector, clave), que además cuente las comparaciones
#    que hizo.
# 2. Con el vector [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], completar la tabla.
#    La primera fila está resuelta como ejemplo:
#      Clave 20 -> Sin corte: 10, Con corte: 6
# 3. ¿En qué casos el corte no ahorra ninguna comparación?
#
# ------------------------------------------------------------------------------
# RESPUESTA AL PUNTO 3:
# ¿En qué casos el corte no ahorra ninguna comparación?
# 1. Cuando la clave está en el vector: ambas búsquedas se detienen exactamente
#    en la posición del elemento, realizando la misma cantidad de comparaciones.
# 2. Cuando la clave NO está en el vector, pero es mayor que el último elemento
#    (por ejemplo, la clave 100): ambas búsquedas tienen que recorrer todo el
#    vector hasta el final (10 comparaciones).
# ==============================================================================


def secuencial_sin_corte(vector, clave):
    """
    Búsqueda secuencial estándar (corta sólo si encuentra el elemento).
    Retorna una tupla: (posicion_encontrada, cantidad_comparaciones)
    """
    comparaciones = 0
    posicion = -1
    for i in range(len(vector)):
        comparaciones = comparaciones + 1
        if vector[i] == clave:
            posicion = i
            break
    return posicion, comparaciones


def secuencial_con_corte(vector, clave):
    """
    Búsqueda secuencial en vector ordenado de menor a mayor.
    Corta si encuentra el elemento o si encuentra un elemento mayor a la clave.
    Retorna una tupla: (posicion_encontrada, cantidad_comparaciones)
    """
    comparaciones = 0
    posicion = -1
    for i in range(len(vector)):
        comparaciones = comparaciones + 1
        if vector[i] == clave:
            posicion = i
            break
        elif vector[i] > clave:
            # Como el vector está ordenado de menor a mayor, todos los
            # elementos siguientes serán mayores, por lo tanto no estará.
            break
    return posicion, comparaciones


# ==============================================================================
# PROGRAMA PRINCIPAL Y GENERACIÓN DE LA TABLA
# ==============================================================================

vector_ordenado = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
claves_a_probar = [20, 1, 56, 100]

print("==================================================================")
print("   EJERCICIO 2: SECUENCIAL CON CORTE EN UN VECTOR ORDENADO        ")
print("==================================================================")
print(f"Vector ordenado de prueba: {vector_ordenado}\n")

print(f"{'Clave':<8} {'Comparaciones sin corte':<26} {'Comparaciones con corte':<26}")
print("-" * 62)

for clave in claves_a_probar:
    pos_sin, comp_sin = secuencial_sin_corte(vector_ordenado, clave)
    pos_con, comp_con = secuencial_con_corte(vector_ordenado, clave)
    print(f"{clave:<8} {comp_sin:<26} {comp_con:<26}")

print("-" * 62)

print("\n--- DETALLE DE CADA CASO ---")
print("• Clave 20: No está. Sin corte revisa los 10 elementos. Con corte corta en el 23 (6 comparaciones).")
print("• Clave 1:  No está. Sin corte revisa los 10 elementos. Con corte corta en el 2 (1 comparación).")
print("• Clave 56: Sí está (índice 7). Ambas búsquedas se detienen al encontrarlo en 8 comparaciones.")
print("• Clave 100: No está. Como 100 > 91 (el mayor), ambas revisan todo el vector (10 comparaciones).")

print("\n--- RESPUESTA A LA PREGUNTA 3 ---")
print("¿En qué casos el corte no ahorra ninguna comparación?")
print("1. Cuando el elemento SÍ está en el vector (ambas se detienen en la misma posición).")
print("2. Cuando el elemento NO está, pero es mayor que todos los elementos del vector")
print("   (por lo que nunca encuentra un valor mayor y debe llegar hasta el final).")
