from pathlib import Path
from calculadora_matrices.matrices.matriz import Matriz

# python -m calculadora_matrices.io.lectura

def read_file():
    archivo = Path(__file__).parent / ".." / "resources" / "matrices" / "matriz.txt"

    with open(archivo.resolve(), "r") as file:
        lineas = file.readlines()

        matrices = []
        values = []

        for linea in lineas:
            if linea.strip() == "":
                # Si es una linea vacia entonces se guarda como una matriz
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

        # guardar la última matriz (si no termina en línea vacía)
        if values:
            matrices.append(Matriz(values))

    return matrices

def ver_matrices():
    print("Estas son las matrices guardadas")
    matrices = read_file()
    for i in range(len(matrices)):
        print(f"Matriz numero {i + 1}")
        print(matrices[i])