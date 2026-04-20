from calculadora_matrices.io.input_validation import guardar_matriz, ver_matrices, elegir
from calculadora_matrices.matrices.operaciones import suma, resta, mult_escalar, mult_matrices, inversa, transpuesta, resolver_sistema
from calculadora_matrices.io.lectura import read_file

if __name__ == "__main__":
    while True:
        print("\n===== MENU =====")
        print("1) Introducir matrices")
        print("2) Ver matrices guardadas")
        print("3) Suma")
        print("4) Resta")
        print("5) Multiplicacion por ecalar")
        print("6) Multiplicacion de matrices")
        print("7) Matriz inversa")
        print("8) Matriz transpuesta")
        print("9) Solucion de un sistema")
        print("0) Salir")

        while True:
            try:
                opcion = int(input("Elige opción (0-9): "))

                if opcion < 0 or opcion > 9:
                    raise ValueError("Opción fuera de rango")
                break

            except ValueError as e:
                print(e)
            

        if opcion == 0:
            break
        elif opcion == 1:
            guardar_matriz()
        elif opcion == 2:
            ver_matrices()

        # SUMA
        elif opcion == 3:
            print("\n===== Suma =====")
            matrices = read_file()
            A = elegir("la primera matriz", len(matrices))
            B = elegir("la segunda matriz", len(matrices))

            try:
                C = suma(matrices[A - 1], matrices[B - 1])
                print(C)
            except ValueError as e:
                print("Error:", e)

        # RESTA
        elif opcion == 4:
            print("\n===== Resta =====")
            matrices = read_file()
            A = elegir("la primera matriz", len(matrices))
            B = elegir("la segunda matriz", len(matrices))

            try:
                print(resta(matrices[A - 1], matrices[B - 1]))
            except ValueError as e:
                print("Error:", e)

        # MULTIPLICACION POR ESCALAR
        elif opcion == 5:
            print("\n===== Multiplicacion por Escalar =====")
            matrices = read_file()
            A = elegir("la matriz", len(matrices))
            x = elegir("el escalar", len(matrices))

            try:
                print(mult_escalar(matrices[A - 1], matrices[x - 1]))
            except ValueError as e:
                print("Error:", e)

        # MULTIPLICACION DE MATRICES
        elif opcion == 6:
            print("\n===== Multiplicacion de Matrices =====")
            matrices = read_file()
            A = elegir("la primera matriz", len(matrices))
            B = elegir("la segunda matriz", len(matrices))

            try:
                print(mult_matrices(matrices[A - 1], matrices[B - 1]))
            except ValueError as e:
                print("Error:", e)

        # MATRIZ INVERSA
        elif opcion == 7:
            print("\n===== Matriz Inversa =====")
            matrices = read_file()
            A = elegir("la matriz", len(matrices))

            try:
                print(inversa(matrices[A - 1]))
            except ValueError as e:
                print("Error:", e)

        # MATRIZ TRANSPUESTA
        elif opcion == 8:
            print("\n===== Matriz Transpuesta =====")
            matrices = read_file()
            A = elegir("la matriz", len(matrices))

            print(transpuesta(matrices[A - 1]))

        # SISTEMA Ax = b
        elif opcion == 9:
            print("\n===== Solucion de un Sistema =====")
            matrices = read_file()
            A = elegir("la matriz A", len(matrices))
            b = elegir("el vector b", len(matrices))

            try:
                print(resolver_sistema(matrices[A - 1], matrices[b - 1]))
            except ValueError as e:
                print("Error:", e)
            