# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 6 – Transformación de claves (Hash con Sondeo Lineal)
# ==============================================================================
#
# Consigna:
# Un almacén identifica sus productos con códigos numéricos y los guarda en una tabla
# hash de 13 posiciones, con la función h(código) = código % 13. Las colisiones se
# resuelven con sondeo lineal.
#
# 1. En papel: insertar en este orden los códigos 15, 28, 9, 41, 22, 36 y 12.
#    Dibujar la tabla final e indicar qué códigos colisionaron.
# 2. En papel: indicar qué casillas se miran al buscar 36, 54 y 25, y el resultado de cada búsqueda.
# 3. En Python: programar insertar(tabla, codigo) y buscar_hash(tabla, codigo),
#    con la tabla inicializada como [None] * 13, y comprobar los resultados de los puntos 1 y 2.
# 4. ¿Qué tiene que pasar cuando el sondeo llega a la última posición de la tabla?
#    ¿Qué parte del código se encarga de eso?
#
# ------------------------------------------------------------------------------
# RESPUESTA AL PUNTO 1 (En papel):
# Inserciones:
# • 15: 15 % 13 = 2  -> Guarda en casilla 2 (Sin colisión)
# • 28: 28 % 13 = 2  -> Ocupada (COLISIÓN con 15). Sondeo lineal a casilla 3 -> Guarda en 3
# •  9:  9 % 13 = 9  -> Guarda en casilla 9 (Sin colisión)
# • 41: 41 % 13 = 2  -> Ocupada (COLISIÓN con 15). Casilla 3 ocupada (COLISIÓN con 28).
#                       Sondeo a casilla 4 -> Guarda en 4
# • 22: 22 % 13 = 9  -> Ocupada (COLISIÓN con 9). Sondeo a casilla 10 -> Guarda en 10
# • 36: 36 % 13 = 10 -> Ocupada (COLISIÓN con 22). Sondeo a casilla 11 -> Guarda en 11
# • 12: 12 % 13 = 12 -> Guarda en casilla 12 (Sin colisión)
#
# Códigos que colisionaron: 28, 41, 22 y 36.
#
# ------------------------------------------------------------------------------
# RESPUESTA AL PUNTO 2 (En papel):
# • Buscar 36: h(36) = 10.
#   Mira casilla 10 (hay 22) -> Mira casilla 11 (está 36).
#   Casillas miradas: [10, 11]. Resultado: Encontrado en posición 11.
# • Buscar 54: h(54) = 2.
#   Mira casilla 2 (15) -> Casilla 3 (28) -> Casilla 4 (41) -> Casilla 5 (None / vacía).
#   Casillas miradas: [2, 3, 4, 5]. Resultado: No encontrado (termina al hallar None).
# • Buscar 25: h(25) = 12.
#   Mira casilla 12 (12) -> Da la vuelta al inicio: Casilla 0 (None / vacía).
#   Casillas miradas: [12, 0]. Resultado: No encontrado.
#
# ------------------------------------------------------------------------------
# RESPUESTA AL PUNTO 4:
# ¿Qué tiene que pasar cuando el sondeo llega a la última posición de la tabla?
# Debe volver a empezar desde el principio de la tabla (posición 0), de forma circular.
# ¿Qué parte del código se encarga de eso?
# La expresión de avance circular con el operador módulo (%):
#    pos = (pos + 1) % len(tabla)
# ==============================================================================


def h(codigo, tamano=13):
    """Función de dispersión (hash): código % tamaño."""
    return codigo % tamano


def insertar(tabla, codigo):
    """
    Inserta 'codigo' en la 'tabla' hash usando resolución por sondeo lineal.
    Retorna la posición donde se insertó o -1 si la tabla está llena.
    """
    tamano = len(tabla)
    pos = h(codigo, tamano)
    intentos = 0

    while tabla[pos] is not None and intentos < tamano:
        # Si ya está el mismo código no lo duplicamos
        if tabla[pos] == codigo:
            return pos
        # Sondeo lineal circular
        pos = (pos + 1) % tamano
        intentos = intentos + 1

    if intentos < tamano:
        tabla[pos] = codigo
        return pos
    else:
        print(f"Error: La tabla hash está llena, no se pudo insertar {codigo}.")
        return -1


def buscar_hash(tabla, codigo):
    """
    Busca 'codigo' en la 'tabla' hash con sondeo lineal.
    Retorna una tupla: (posicion_o_menos_uno, lista_de_casillas_examinadas).
    """
    tamano = len(tabla)
    pos = h(codigo, tamano)
    casillas_miradas = []
    intentos = 0

    while tabla[pos] is not None and intentos < tamano:
        casillas_miradas.append(pos)
        if tabla[pos] == codigo:
            return pos, casillas_miradas
        pos = (pos + 1) % tamano
        intentos = intentos + 1

    # Si se detuvo en una casilla vacía dentro del rango, registramos esa casilla observada
    if intentos < tamano:
        casillas_miradas.append(pos)

    return -1, casillas_miradas


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

tabla = [None] * 13
codigos_a_insertar = [15, 28, 9, 41, 22, 36, 12]

print("=========================================================================")
print("          EJERCICIO 6: TRANSFORMACIÓN DE CLAVES (HASHING)                ")
print("=========================================================================")

print("\n--- PASO 1: INSERTANDO CÓDIGOS ---")
colisiones = []

for cod in codigos_a_insertar:
    casilla_ideal = h(cod, len(tabla))
    casilla_real = insertar(tabla, cod)
    if casilla_real != casilla_ideal:
        colisiones.append(cod)
        print(f"Código {cod:>2}: h({cod}) = {casilla_ideal:>2} -> ¡COLISIÓN! Se ubicó en casilla {casilla_real:>2} por sondeo.")
    else:
        print(f"Código {cod:>2}: h({cod}) = {casilla_ideal:>2} -> Ubicado directamente en casilla {casilla_real:>2}.")

print(f"\nCódigos que colisionaron: {colisiones}")

print("\n--- ESTADO FINAL DE LA TABLA HASH (13 CASILLAS) ---")
print(f"{'Índice':<8} {'Contenido':<15}")
print("-" * 25)
for i in range(len(tabla)):
    contenido = str(tabla[i]) if tabla[i] is not None else "None (vacío)"
    print(f"[{i:>2}]     {contenido}")
print("-" * 25)

print("\n--- PASO 2: BÚSQUEDAS DE PRUEBA (36, 54, 25) ---")
codigos_buscar = [36, 54, 25]

for cod in codigos_buscar:
    pos_hallada, casillas = buscar_hash(tabla, cod)
    if pos_hallada != -1:
        resultado = f"Encontrado en posición {pos_hallada}"
    else:
        resultado = "No encontrado (no está en la tabla)"
    print(f"• Búsqueda de {cod:>2}: Casillas miradas: {casillas} -> Resultado: {resultado}")

print("\n--- RESPUESTA A LA PREGUNTA 4 ---")
print("¿Qué tiene que pasar cuando el sondeo llega a la última posición de la tabla?")
print("Respuesta: El sondeo debe reiniciar de forma circular desde la primera posición (índice 0).")
print("¿Qué parte del código se encarga de eso?")
print("Respuesta: La operación de módulo: 'pos = (pos + 1) % len(tabla)'.")
