archivoProductos = "productos.txt"
archivoVentas = "ventas.txt"
diasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


def buscarProductoPorCodigo(codigo, productos):
    indiceEncontrado = -1
    for i in range(len(productos)):
        if productos[i]["codigo"] == codigo:
            indiceEncontrado = i
            break
    return indiceEncontrado


def calcularTotalUnidadesProducto(indiceProd, matrizVentas):
    totalUnidades = 0
    for dia in range(5):
        totalUnidades = totalUnidades + matrizVentas[indiceProd][dia]
    return totalUnidades


def calcularRecaudacionDia(dia, productos, matrizVentas):
    columnaDia = dia - 1
    recaudacion = 0.0
    for i in range(len(productos)):
        cantidad = matrizVentas[i][columnaDia]
        precio = productos[i]["precio"]
        recaudacion = recaudacion + (cantidad * precio)
    return recaudacion


def calcularRecaudacionTotalSemana(productos, matrizVentas):
    totalSemana = 0.0
    for dia in range(1, 6):
        totalSemana = totalSemana + calcularRecaudacionDia(dia, productos, matrizVentas)
    return totalSemana


def inicializarMatrizVentas(cantidadProductos, cantidadDias=5):
    matriz = []
    for _ in range(cantidadProductos):
        fila = [0] * cantidadDias
        matriz.append(fila)
    return matriz


def cargarProductosDesdeArchivo(nombreArchivo):
    try:
        with open(nombreArchivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            productos = []
            for linea in lineas:
                lineaLimpia = linea.strip()
                if lineaLimpia != "":
                    partes = lineaLimpia.split(",")
                    if len(partes) == 3:
                        codigo = int(partes[0])
                        nombre = partes[1]
                        precio = float(partes[2])
                        productos.append({"codigo": codigo, "nombre": nombre, "precio": precio})
            if len(productos) == 0:
                raise FileNotFoundError
            return productos
    except FileNotFoundError:
        catalogoInicial = [
            {"codigo": 101, "nombre": "Café con leche", "precio": 1500.0},
            {"codigo": 102, "nombre": "Medialuna", "precio": 700.0},
            {"codigo": 103, "nombre": "Sándwich de miga", "precio": 1800.0},
            {"codigo": 104, "nombre": "Agua mineral 500 ml", "precio": 1000.0},
            {"codigo": 105, "nombre": "Empanada", "precio": 1200.0},
            {"codigo": 106, "nombre": "Chipá (100 g)", "precio": 1300.0}
        ]
        with open(nombreArchivo, "w", encoding="utf-8") as f:
            for p in catalogoInicial:
                f.write(f"{p['codigo']},{p['nombre']},{p['precio']}\n")
        return catalogoInicial


def mostrarCatalogo(productos):
    print("\n----------------- CATÁLOGO DE PRODUCTOS -----------------")
    print(f"{'Código':<8} {'Producto':<25} {'Precio ($)':>10}")
    print("-" * 47)
    for p in productos:
        print(f"{p['codigo']:<8} {p['nombre']:<25} ${p['precio']:>9.2f}")
    print("-" * 47)


def guardarProductoEnArchivo(producto, nombreArchivo):
    linea = f"{producto['codigo']},{producto['nombre']},{producto['precio']}\n"
    with open(nombreArchivo, "a", encoding="utf-8") as f:
        f.write(linea)


def guardarVentaEnArchivo(dia, codigo, cantidad, nombreArchivo):
    linea = f"{dia},{codigo},{cantidad}\n"
    with open(nombreArchivo, "a", encoding="utf-8") as f:
        f.write(linea)


def cargarVentasEnMatriz(nombreArchivo, productos, matrizVentas):
    try:
        with open(nombreArchivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            for linea in lineas:
                lineaLimpia = linea.strip()
                if lineaLimpia != "":
                    partes = lineaLimpia.split(",")
                    if len(partes) == 3:
                        dia = int(partes[0])
                        codigo = int(partes[1])
                        cantidad = int(partes[2])
                        indiceProd = buscarProductoPorCodigo(codigo, productos)
                        if indiceProd != -1 and 1 <= dia <= 5:
                            columnaDia = dia - 1
                            matrizVentas[indiceProd][columnaDia] += cantidad
    except FileNotFoundError:
        pass


def registrarVenta(productos, matrizVentas, nombreArchivoVentas):
    print("\n>>> REGISTRAR VENTA <<<")
    diaValido = False
    dia = 0
    while not diaValido:
        try:
            print("\nDías: 1=Lunes, 2=Martes, 3=Miércoles, 4=Jueves, 5=Viernes")
            dia = int(input("Ingrese el día (1 a 5): "))
            if 1 <= dia <= 5:
                diaValido = True
            else:
                print("Error: El día debe estar entre 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

    codigoValido = False
    indiceProd = -1
    codigo = 0
    while not codigoValido:
        try:
            codigo = int(input("Ingrese el código del producto: "))
            indiceProd = buscarProductoPorCodigo(codigo, productos)
            if indiceProd != -1:
                codigoValido = True
            else:
                print(f"Error: El código {codigo} no existe en el catálogo.")
                opcionReintentar = input("¿Desea ver el catálogo de productos? (s/n): ").lower()
                if opcionReintentar == "s":
                    mostrarCatalogo(productos)
        except ValueError:
            print("Error: Debe ingresar un código numérico.")

    cantidadValida = False
    cantidad = 0
    while not cantidadValida:
        try:
            cantidad = int(input(f"Ingrese la cantidad vendida de '{productos[indiceProd]['nombre']}': "))
            if cantidad > 0:
                cantidadValida = True
            else:
                print("Error: La cantidad vendida debe ser mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero positivo.")

    columnaDia = dia - 1
    matrizVentas[indiceProd][columnaDia] += cantidad
    guardarVentaEnArchivo(dia, codigo, cantidad, nombreArchivoVentas)

    subtotal = cantidad * productos[indiceProd]["precio"]
    print(f"\n[Éxito] Venta registrada:")
    print(f"Día: {diasSemana[columnaDia]} | Producto: {productos[indiceProd]['nombre']} | Cantidad: {cantidad} | Importe: ${subtotal:.2f}")


def cargarNuevoProducto(productos, matrizVentas, nombreArchivoProductos):
    print("\n>>> CARGAR NUEVO PRODUCTO AL CATÁLOGO <<<")
    codigoValido = False
    codigo = 0
    while not codigoValido:
        try:
            codigo = int(input("Ingrese el nuevo código del producto: "))
            if codigo <= 0:
                print("Error: El código debe ser mayor a 0.")
            elif buscarProductoPorCodigo(codigo, productos) != -1:
                print(f"Error: Ya existe un producto con el código {codigo}. No se permiten duplicados.")
            else:
                codigoValido = True
        except ValueError:
            print("Error: Debe ingresar un número entero.")

    nombre = input("Ingrese el nombre del producto: ").strip()
    while nombre == "":
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del producto: ").strip()

    precioValido = False
    precio = 0.0
    while not precioValido:
        try:
            precio = float(input("Ingrese el precio unitario ($): "))
            if precio > 0:
                precioValido = True
            else:
                print("Error: El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un importe numérico válido.")

    nuevoProducto = {"codigo": codigo, "nombre": nombre, "precio": precio}
    productos.append(nuevoProducto)
    matrizVentas.append([0, 0, 0, 0, 0])
    guardarProductoEnArchivo(nuevoProducto, nombreArchivoProductos)
    print(f"\n[Éxito] Producto '{nombre}' (código {codigo}) guardado correctamente en el catálogo.")


def mostrarInformes(productos, matrizVentas):
    print("\n========================================================")
    print("           INFORMES DE VENTAS DE LA SEMANA              ")
    print("========================================================")

    print("\n[INFORME 1] UNIDADES VENDIDAS DE CADA PRODUCTO")
    print(f"{'Código':<8} {'Producto':<25} {'Unidades Vendidas':>18}")
    print("-" * 53)
    
    totalesPorProducto = []
    totalUnidadesSemana = 0
    for i in range(len(productos)):
        totalProd = calcularTotalUnidadesProducto(i, matrizVentas)
        totalesPorProducto.append(totalProd)
        totalUnidadesSemana += totalProd
        print(f"{productos[i]['codigo']:<8} {productos[i]['nombre']:<25} {totalProd:>18}")
    print(f"Total general de unidades vendidas en la semana: {totalUnidadesSemana}")

    print("\n[INFORME 2] RECAUDACIÓN DE CADA DÍA")
    print(f"{'Día':<12} {'Recaudación ($)':>18}")
    
    recaudacionesPorDia = []
    for dia in range(1, 6):
        recDia = calcularRecaudacionDia(dia, productos, matrizVentas)
        recaudacionesPorDia.append(recDia)
        nombreDia = diasSemana[dia - 1]
        print(f"{nombreDia:<12} ${recDia:>17.2f}")

    print("\n[INFORME 3] DESTACADOS DE LA SEMANA")

    if totalUnidadesSemana == 0:
        print("  - Producto más vendido: No hubo ventas registradas esta semana.")
    else:
        maxUnidades = max(totalesPorProducto)
        productosMasVendidos = []
        for i in range(len(productos)):
            if totalesPorProducto[i] == maxUnidades:
                productosMasVendidos.append(productos[i]["nombre"])
        
        if len(productosMasVendidos) == 1:
            print(f"  - Producto más vendido: {productosMasVendidos[0]} ({maxUnidades} unidades)")
        else:
            print(f"  - Producto más vendido (EMPATE con {maxUnidades} unidades):")
            for nombreP in productosMasVendidos:
                print(f"      * {nombreP}")

    recaudacionTotal = sum(recaudacionesPorDia)
    if recaudacionTotal == 0.0:
        print("  - Día de mayor recaudación: No hubo recaudación esta semana ($0.00).")
    else:
        maxRecaudacion = max(recaudacionesPorDia)
        diasMayorRecaudacion = []
        for d in range(5):
            if recaudacionesPorDia[d] == maxRecaudacion:
                diasMayorRecaudacion.append(diasSemana[d])
        
        if len(diasMayorRecaudacion) == 1:
            print(f"  - Día de mayor recaudación: {diasMayorRecaudacion[0]} (${maxRecaudacion:.2f})")
        else:
            print(f"  - Día de mayor recaudación (EMPATE con ${maxRecaudacion:.2f}):")
            for diaNombre in diasMayorRecaudacion:
                print(f"      * {diaNombre}")

    print("\n[INFORME 4] PRODUCTOS SIN VENTAS (0 UNIDADES)")
    productosSinVentas = []
    for i in range(len(productos)):
        if totalesPorProducto[i] == 0:
            productosSinVentas.append(productos[i])
            
    if len(productosSinVentas) == 0:
        print("  Todos los productos del catálogo tuvieron al menos una venta esta semana.")
    else:
        print(f"{'Código':<8} {'Producto':<25}")
        print("-" * 35)
        for p in productosSinVentas:
            print(f"{p['codigo']:<8} {p['nombre']:<25}")

    print("\n[INFORME 5] RECAUDACIÓN TOTAL DE LA SEMANA")
    print(f"  Total recaudado (Lunes a Viernes): ${recaudacionTotal:.2f}")
    print("========================================================\n")


def reiniciarVentasSemana(nombreArchivoVentas, matrizVentas):
    confirmacion = input("\n¿Está seguro de reiniciar todas las ventas de la semana? (s/n): ").lower()
    if confirmacion == "s":
        with open(nombreArchivoVentas, "w", encoding="utf-8") as f:
            f.write("")
        for i in range(len(matrizVentas)):
            for j in range(len(matrizVentas[i])):
                matrizVentas[i][j] = 0
        print("[Aviso] Se han reiniciado todas las ventas de la semana con éxito.")
    else:
        print("Operación cancelada.")



productos = cargarProductosDesdeArchivo(archivoProductos)
matrizVentas = inicializarMatrizVentas(len(productos), 5)
cargarVentasEnMatriz(archivoVentas, productos, matrizVentas)

opcion = 0
while opcion != 6:
    print("\n========================================")
    print("    EL BUFFET DE LA FACULTAD - MARTA    ")
    print("========================================")
    print("1. Ver catálogo de productos")
    print("2. Cargar nuevo producto al catálogo")
    print("3. Registrar una venta")
    print("4. Ver informes de la semana")
    print("5. Reiniciar ventas (Nueva semana)")
    print("6. Salir")
        
    try:
        opcion = int(input("\nSeleccione una opción (1-6): "))
    except ValueError:
        print("Por favor, ingrese un número válido del 1 al 6.")
        continue

    if opcion == 1:
        mostrarCatalogo(productos)
    elif opcion == 2:
        cargarNuevoProducto(productos, matrizVentas, archivoProductos)
    elif opcion == 3:
        registrarVenta(productos, matrizVentas, archivoVentas)
    elif opcion == 4:
        mostrarInformes(productos, matrizVentas)
    elif opcion == 5:
        reiniciarVentasSemana(archivoVentas, matrizVentas)
    elif opcion == 6:
        print("\nGracias por usar el sistema del Buffet.")
        break
    else:
        print("\nOpción no válida. Por favor seleccione un número del 1 al 6.")
