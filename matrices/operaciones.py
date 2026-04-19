from matriz import Matriz

# Suma y resta
def suma(A, B):
    if A.rows != B.rows or A.cols != B.cols:
        raise ValueError(f"Las matrices no son del mismo tamaño")
    
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j] + B[i][j])
        values.append(row)

    return Matriz(values)

def resta(A, B):
    if A.rows != B.rows or A.cols != B.cols:
        raise ValueError(f"Las matrices no son del mismo tamaño")
    
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j] - B[i][j])
        values.append(row)

    return Matriz(values)

# Multiplicacion por escalar
def mult_escalar(A, escalar):
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j] * escalar)
        values.append(row)

    return Matriz(values)

# Multiplicacion de matrices
def mult_matrices(A, B):
    if A.cols != B.rows:
        raise ValueError(f"Las columnas de la matriz deben ser iguales a las filas de B.")
    
    values = []

    for i in range(A.rows):
        row = []
        for j in range(B.cols):
            suma = 0
            for k in range(A.cols):
                suma += A[i][k] * B[k][j]
            row.append(suma)
        values.append(row)
    
    return Matriz(values)

# Determinante de matrices
def det_2x2(A):
    if A.rows!= 2 and A.cols != 2:
        raise ValueError(f"Las columnas y filas de la matriz deben ser 2.")
    
    return A[0][0] * A[1][1] - A[1][0] * A[0][1]
                    
def cortar_incorrecto(A, nivel_row):
    matrices = []
    for i in range(nivel_row):
        print(f"\n" + "="*20 + "FILA " + str(i) + "="*20)
        for j in range(A.cols):
            values = []
            for k in range(A.rows):
                print(f"\n" + "="*20 + "MITRAZ " + str(k) + "="*20)
                row = []
                for l in range(A.cols):
                    print(f"({i}, {j}), ({k}, {l})")
                    if i != k and j != l:
                        row.append(A[k][j])
                        print("distinto")
                    else:
                        print("igual")
            
                if len(row) != 0:
                    values.append(row)

            matrices.append(Matriz(values))
            print(Matriz(values))

    return matrices

def cortar(A, nivel_row):
    matrices = []
    for i in range(nivel_row):
        for j in range(A.cols):
            values = []
            for k in range(A.rows):
                row = []
                for l in range(A.cols):
                    if i != k and j != l:
                        row.append(A[k][l])
                if len(row) != 0:
                    values.append(row)
            matrices.append(values)

    # Las matrices se devuelven como una lista de matrices
    return matrices

def det(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        matrices = cortar(A, 1)
    if A.rows == 2:
        return det_2x2(A)
    if A.rows == 1:
        return A.values
    
    suma = 0
    for i in range(A.cols):
        suma += (-1)**(i + 2) * A[0][i] * det(Matriz(matrices[i]))
    return suma

# Adjunta
def adjunta2(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        matrices = Matriz(cortar(A, A.cols))

    values = []
    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append((-1)**(i+ j + 2) * A[i][j] * det(Matriz(matrices[i][j])))
        values.append(row)

    return Matriz(values)

def adjunta(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        for i in range(A.rows):
            matrices = cortar(A, i + 1)
            for j in range(A.cols):
                matriz  (-1)**(i + 2) * A[0][i] * det(matrices[j])

        

def adjunta1(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        matrices = cortar(A, nivel_row)
    if A.rows == 2:
        return det_2x2(A)
    if A.rows == 1:
        return A.values

    values = []
    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append((-1)**(i + j + 2) * det(matrices[j], i))
        values.append(row)
    return Matriz(values)

# Matriz inversa
def inversa(A):
    return 


# Matriz transpuesta
def transpuesta(A):
    values = []

    for i in range(A.cols):
        row = []
        for j in range(A.rows):
            row.append(A[j][i])
        values.append(row)

    return Matriz(values)

A = Matriz([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

B = Matriz([[7, 2], [-1, 4]])

C = Matriz((["a", "b", "c", "d"],
            ["e", "f", "g", "h"],
            ["i", "j", "k", "l"],
            ["m", "n", "o", "p"]))

print(Matriz(adjunta2(A)))
# for matriz in cortar(A, A.rows):
#   print(f"{matriz}\n")