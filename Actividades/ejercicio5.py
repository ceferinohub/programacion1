# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 5 – ¿Cuál conviene?
# ==============================================================================
#
# Consigna:
# Armar con un ciclo un vector con los múltiplos de 3 desde 3 hasta 3000 (1.000 elementos).
# Programar versiones de la búsqueda secuencial y de la binaria que devuelvan la
# posición y la cantidad de comparaciones. Se cuenta una comparación por cada
# elemento que se mira, es decir, una por vuelta del ciclo.
#
# Completar la tabla. La primera fila está resuelta como ejemplo:
#   Clave: 3 | Posición: 0 | Comp. Secuencial: 1 | Comp. Binaria: 9
#
# Claves a evaluar: 3, 1500, 2001, 3000, 1000.
#
# Según la tabla, ¿cuándo conviene cada método? Tengan en cuenta que la binaria
# exige que el vector esté ordenado.
#
# ------------------------------------------------------------------------------
# RESPUESTA A LA PREGUNTA FINAL:
# ¿Cuándo conviene cada método?
# 1. La Búsqueda Binaria conviene cuando el vector ya está ordenado o se van a
#    realizar muchas búsquedas sobre la misma estructura. Su eficiencia es
#    inmensamente superior (complejidad O(log n)), requiriendo a lo sumo 10
#    comparaciones para 1.000 elementos, mientras que la secuencial puede requerir
#    hasta 1.000 comparaciones.
# 2. La Búsqueda Secuencial sólo conviene:
#    - Si el vector está desordenado y se va a hacer una búsqueda esporádica
#      (ya que ordenar el vector costaría más tiempo que buscar directamente).
#    - Si se busca un elemento que con alta probabilidad está en los primeros
#      lugares del vector (por ejemplo la clave 3, donde la secuencial tardó 1
#      comparación y la binaria 9).
# ==============================================================================


def busqueda_secuencial_con_contador(vector, clave):
    """
    Búsqueda secuencial contando una comparación por cada elemento examinado.
    Retorna (posicion, comparaciones).
    """
    comparaciones = 0
    posicion = -1
    for i in range(len(vector)):
        comparaciones = comparaciones + 1
        if vector[i] == clave:
            posicion = i
            break
    return posicion, comparaciones


def busqueda_binaria_con_contador(vector, clave):
    """
    Búsqueda binaria contando una comparación por cada vuelta de ciclo.
    Retorna (posicion, comparaciones).
    """
    comparaciones = 0
    posicion = -1
    inicio = 0
    fin = len(vector) - 1

    while inicio <= fin:
        comparaciones = comparaciones + 1
        medio = (inicio + fin) // 2

        if vector[medio] == clave:
            posicion = medio
            break
        elif clave > vector[medio]:
            inicio = medio + 1
        else:
            fin = medio - 1

    return posicion, comparaciones


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

# 1. Armamos el vector con un ciclo (múltiplos de 3 desde 3 hasta 3000)
vector_multiplos = []
for i in range(1, 1001):
    vector_multiplos.append(i * 3)

claves_evaluar = [3, 1500, 2001, 3000, 1000]

print("=======================================================================================")
print("                   EJERCICIO 5: COMPARACIÓN DE MÉTODOS DE BÚSQUEDA                     ")
print("=======================================================================================")
print(f"Cantidad de elementos generados en el vector: {len(vector_multiplos)}")
print(f"Primer elemento: {vector_multiplos[0]} | Último elemento: {vector_multiplos[-1]}\n")

# Encabezado de la tabla
print(f"{'Clave':<8} {'Posición':<12} {'Comparaciones secuencial':<26} {'Comparaciones binaria':<24}")
print("-" * 72)

for clave in claves_evaluar:
    pos_sec, comp_sec = busqueda_secuencial_con_contador(vector_multiplos, clave)
    pos_bin, comp_bin = busqueda_binaria_con_contador(vector_multiplos, clave)

    pos_texto = str(pos_sec) if pos_sec != -1 else "No está (-1)"

    print(f"{clave:<8} {pos_texto:<12} {comp_sec:<26} {comp_bin:<24}")

print("-" * 72)

print("\n--- ANÁLISIS DE LA TABLA Y CONCLUSIONES ---")
print("• Clave 3:    Está al inicio. La secuencial gana (1 comp vs 9 de la binaria).")
print("• Clave 1500: Justo en el medio. La binaria la encuentra en 1 comp (la secuencial necesita 500).")
print("• Clave 2001: La binaria requiere sólo 8 comp frente a 667 de la secuencial.")
print("• Clave 3000: Al final del vector. La binaria requiere 10 comp frente a 1.000 de la secuencial.")
print("• Clave 1000: No está en el vector. La binaria lo descarta en 10 comp frente a 1.000 de la secuencial.")

print("\n--- RESPUESTA A LA PREGUNTA ---")
print("¿Cuándo conviene cada método?")
print("1. La búsqueda binaria conviene prácticamente siempre en vectores ordenados o cuando se")
print("   van a realizar búsquedas repetidas, porque su crecimiento es logarítmico (máximo 10 comparaciones).")
print("2. La búsqueda secuencial conviene cuando el vector está desordenado y no vale la pena ordenarlo")
print("   para una sola búsqueda, o si sabemos que el dato buscado suele encontrarse en las primeras posiciones.")
