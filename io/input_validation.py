from pathlib import Path
from calculadora_matrices.io.lectura import read_file
from calculadora_matrices.matrices.matriz import Matriz

def guardar_matriz():
    print("Introduce la matriz (ENTER vacío para terminar)")
    print("'Los vectores y escalares se tomaran como matrices'\n")

    archivo = Path(__file__).parent / ".." / "resources" / "matrices" / "matriz.txt"

    with open(archivo.resolve(), "a") as file:
        while True:
            linea = input()

            if linea.strip() == "":
                file.write("\n")
                break

            file.write(linea + "\n")  # guarda la línea

    print("Matriz guardada correctamente.")

def elegir(mensaje, maximo):
    while True:
        try:
            matriz = int(input(f"Elige {mensaje} (1-{maximo}): "))
            
            if matriz < 1 or matriz > maximo:
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)

    return matriz

def write_file(matrices, ruta_archivo):
    ruta = Path(ruta_archivo)

    # Si es una sola matriz → convertir a lista
    if isinstance(matrices, Matriz):
        matrices = [matrices]

    with open(ruta, "a") as file:
        for idx, matriz in enumerate(matrices):
            for fila in matriz.values:
                linea = " ".join(str(x) for x in fila)
                file.write(linea + "\n")

            if idx != len(matrices) - 1:
                file.write("\n")

def guardar_resultado(resultado):
    opcion = input("¿Quieres guardar el resultado? (s/n): ").lower()

    if opcion == "s":
        ruta = input("Ingresa la ruta del archivo: ")

        if not ruta.endswith(".txt"):
            print("Error: el archivo debe tener extensión .txt")
            return

        try:
            write_file(resultado, ruta)
            print("Resultado guardado correctamente")
        except Exception as e:
            print("Error al guardar:", e)