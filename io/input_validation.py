from pathlib import Path
from calculadora_matrices.io.lectura import read_file

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

def ver_matrices():
    print("Estas son las matrices guardadas")
    matrices = read_file()
    for i in range(len(matrices)):
        print(f"Matriz numero {i + 1}")
        print(matrices[i])

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