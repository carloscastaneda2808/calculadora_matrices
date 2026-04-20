from pathlib import Path
from calculadora_matrices.matrices.matriz import Matriz

# Guardar matrices de un input
def guardar_matriz():
    ruta = validar_ruta_guardado()

    if ruta is None:
        return

    print("Introduce la matriz (ENTER vacío para terminar)")
    print("'Los vectores y escalares se tomarán como matrices'\n")

    agregar_salto = ruta.exists() and ruta.stat().st_size > 0

    with open(ruta, "a") as file:
        if agregar_salto:
            file.write("\n")

        while True:
            linea = input()

            if linea.strip() == "":
                break

            file.write(linea + "\n")

    print("Matriz guardada correctamente")

# Guardar matrices de un resultado
def guardar_resultado(resultado):
    opcion = input("¿Quieres guardar el resultado? (s/n): ").lower()

    if opcion == "s":
        ruta = validar_ruta_guardado()

        if ruta is None:
            return

        try:
            write_file(resultado, ruta)
            print("Resultado guardado correctamente")
        except Exception as e:
            print("Error al guardar:", e)

# Valida la ruta seleccionada
def validar_ruta_guardado():
    entrada = input("Ingresa la ruta donde guardar: ").strip()

    if not entrada:
        print("ruta inválida")
        return None

    ruta = Path(entrada)

    if ruta.suffix.lower() != ".txt":
        print("Error: el archivo debe tener extensión .txt")
        return None

    # Crear carpetas si no existen
    ruta.parent.mkdir(parents=True, exist_ok=True)

    return ruta

# Escribir el archivo seleccionado
def write_file(matrices, ruta_archivo):
    ruta = Path(ruta_archivo)

    # Si es una sola matriz entonces convertir a lista
    if isinstance(matrices, Matriz):
        matrices = [matrices]

    agregar_salto = ruta.exists() and ruta.stat().st_size > 0

    with open(ruta, "a") as file:
        if agregar_salto:
            file.write("\n")
    
        for idx, matriz in enumerate(matrices):
            for fila in matriz.values:
                linea = " ".join(str(x) for x in fila)
                file.write(linea + "\n")

            if idx != len(matrices) - 1:
                file.write("\n")

# Verifica la seleccion de las matrices para las operaciones
def elegir(mensaje, maximo):
    while True:
        try:
            matriz = int(input(f"Elige {mensaje} (1-{maximo}): "))

            if matriz < 1 or matriz > maximo:
                raise ValueError("Opción fuera de rango")

            return matriz

        except ValueError as e:
            print(e)