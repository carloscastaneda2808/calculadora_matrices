from pathlib import Path
from calculadora_matrices.matrices.matriz import Matriz

# Lee las lineas de un archivo
def read_file(ruta_archivo):
    ruta = Path(ruta_archivo)

    with open(ruta, "r") as file:
        lineas = file.readlines()

        matrices = []
        values = []

        for linea in lineas:
            if linea.strip() == "":
                if values:
                    matrices.append(Matriz(values))
                    values = []
                continue

            elementos = linea.split()
            row = []

            for j in elementos:
                try:
                    row.append(int(j))
                except ValueError:
                    row.append(float(j))

            values.append(row)

        if values:
            matrices.append(Matriz(values))
    
    # Se regresa como una lista de matrices
    return matrices

# Válida la ruta seleccionada
def validar_ruta_lectura():
    while True:
        ruta = Path(input("Ingresa la ruta del archivo a seleccionar: ").strip())

        if not ruta.exists():
            print("Error: el archivo no existe")
            continue

        if ruta.suffix.lower() != ".txt":
            print("Error: el archivo debe ser .txt")
            continue

        return ruta
    
def abrir_matrices():
    ruta = validar_ruta_lectura()
    matrices = read_file(ruta)

    return matrices

# Escribe las matrices
def ver_matrices():
    ruta = validar_ruta_lectura()
    matrices = read_file(ruta)

    print("Estas son las matrices guardadas:\n")

    for i in range(len(matrices)):
        print(f"Matriz numero {i + 1}")
        print(matrices[i])