# ==============================================================================
# PRÁCTICA DE BÚSQUEDA DE DATOS
# Ejercicio 3 – Prueba de escritorio de la búsqueda binaria (en papel)
# ==============================================================================
#
# Vector ordenado dado:
# Índice: 0  1   2   3   4   5   6   7   8   9  10  11  12  13  14
# Valor:  4  9  13  21  26  30  38  45  51  60  67  72  80  88  95
#
# ------------------------------------------------------------------------------
# PRUEBA DE ESCRITORIO PARA CLAVE 67:
# Paso | inicio | fin | medio | vector[medio] | ¿Qué se decide?
# -----+--------+-----+-------+---------------+-------------------------------------
#  1   |   0    | 14  |   7   |      45       | 67 > 45 -> mitad derecha: inicio = 8
#  2   |   8    | 14  |  11   |      72       | 67 < 72 -> mitad izquierda: fin = 10
#  3   |   8    | 10  |   9   |      60       | 67 > 60 -> mitad derecha: inicio = 10
#  4   |  10    | 10  |  10   |      67       | 67 == 67 -> ¡Encontrado en posición 10!
#
# ------------------------------------------------------------------------------
# PRUEBA DE ESCRITORIO PARA CLAVE 10:
# Paso | inicio | fin | medio | vector[medio] | ¿Qué se decide?
# -----+--------+-----+-------+---------------+-------------------------------------
#  1   |   0    | 14  |   7   |      45       | 10 < 45 -> mitad izquierda: fin = 6
#  2   |   0    |  6  |   3   |      21       | 10 < 21 -> mitad izquierda: fin = 2
#  3   |   0    |  2  |   1   |       9       | 10 > 9  -> mitad derecha: inicio = 2
#  4   |   2    |  2  |   2   |      13       | 10 < 13 -> mitad izquierda: fin = 1
# Fin del ciclo: inicio (2) > fin (1) -> No encontrado.
#
# ------------------------------------------------------------------------------
# RESPUESTAS A LAS PREGUNTAS:
# 1. ¿Cuántas comparaciones hizo cada búsqueda?
#    - Para la clave 67: 4 comparaciones (se encontró en el 4to paso).
#    - Para la clave 10: 4 comparaciones (terminó en el 4to paso sin encontrarlo).
#
# 2. Al buscar 10, ¿qué valores tienen inicio y fin cuando termina el ciclo?
#    ¿Qué relación hay entre el valor final de inicio y el lugar donde iría el 10
#    si hubiera que insertarlo en el vector?
#    - Al terminar el ciclo: inicio = 2 y fin = 1.
#    - Relación: El valor final de 'inicio' (2) indica exactamente la posición donde
#      debería insertarse el 10 para que el vector se mantenga ordenado (entre el 9
#      que está en el índice 1 y el 13 que está en el índice 2).
# ==============================================================================


def prueba_escritorio_binaria(vector, clave):
    """
    Simula e imprime paso a paso la prueba de escritorio de la búsqueda binaria
    para una clave dada, siguiendo el formato de la consigna.
    """
    print(f"\n>>> PRUEBA DE ESCRITORIO PARA CLAVE: {clave} <<<")
    print(f"{'Paso':<6} {'inicio':<8} {'fin':<6} {'medio':<7} {'vector[medio]':<15} {'¿Qué se decide?'}")
    print("-" * 75)

    inicio = 0
    fin = len(vector) - 1
    paso = 0
    encontrado = False
    posicion = -1

    while inicio <= fin:
        paso = paso + 1
        medio = (inicio + fin) // 2
        valor_medio = vector[medio]

        if valor_medio == clave:
            decision = f"{clave} == {valor_medio} -> ¡Encontrado en posición {medio}!"
            print(f"{paso:<6} {inicio:<8} {fin:<6} {medio:<7} {valor_medio:<15} {decision}")
            encontrado = True
            posicion = medio
            break
        elif clave > valor_medio:
            decision = f"{clave} > {valor_medio} -> mitad derecha: inicio = {medio + 1}"
            print(f"{paso:<6} {inicio:<8} {fin:<6} {medio:<7} {valor_medio:<15} {decision}")
            inicio = medio + 1
        else:
            decision = f"{clave} < {valor_medio} -> mitad izquierda: fin = {medio - 1}"
            print(f"{paso:<6} {inicio:<8} {fin:<6} {medio:<7} {valor_medio:<15} {decision}")
            fin = medio - 1

    print("-" * 75)
    if not encontrado:
        print(f"El ciclo terminó con inicio = {inicio} y fin = {fin} (inicio > fin).")
        print(f"La clave {clave} no está en el vector.")
    else:
        print(f"La clave {clave} se encontró con éxito en la posición {posicion}.")

    print(f"Total de comparaciones/pasos realizados: {paso}")
    return paso, inicio, fin, posicion


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

vector = [4, 9, 13, 21, 26, 30, 38, 45, 51, 60, 67, 72, 80, 88, 95]

print("===========================================================================")
print("      EJERCICIO 3: PRUEBA DE ESCRITORIO DE LA BÚSQUEDA BINARIA             ")
print("===========================================================================")
print("Vector ordenado:")
for i in range(len(vector)):
    print(f"[{i}]: {vector[i]}", end="  ")
print("\n")

# Ejecutamos las pruebas de escritorio para 67 y 10
pasos_67, ini_67, fin_67, pos_67 = prueba_escritorio_binaria(vector, 67)
pasos_10, ini_10, fin_10, pos_10 = prueba_escritorio_binaria(vector, 10)

print("\n===========================================================================")
print("                     RESPUESTAS A LAS PREGUNTAS                            ")
print("===========================================================================")
print(f"1. ¿Cuántas comparaciones hizo cada búsqueda?")
print(f"   - Para la clave 67: Realizó {pasos_67} comparaciones (encontrado en índice {pos_67}).")
print(f"   - Para la clave 10: Realizó {pasos_10} comparaciones (no encontrado).")

print(f"\n2. Al buscar 10, ¿qué valores tienen inicio y fin cuando termina el ciclo?")
print(f"   Valores finales: inicio = {ini_10}, fin = {fin_10}.")
print(f"   ¿Qué relación hay entre el valor final de inicio y el lugar donde iría el 10")
print(f"   si hubiera que insertarlo en el vector?")
print(f"   Respuesta: El valor final de 'inicio' ({ini_10}) indica la posición exacta")
print(f"   en la que debería insertarse el 10 para mantener el vector ordenado")
print(f"   (quedaría ubicado entre el 9 de la posición 1 y el 13 de la posición 2).")
