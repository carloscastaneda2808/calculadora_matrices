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
                # línea vacía → guardar matriz actual
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

if __name__ == "__main__":
    matrices = read_file()
    for matriz in matrices:
        print(matriz)