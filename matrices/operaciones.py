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

# Inversa
def det_2x2(A):
    if A.rows!= 2 and A.cols != 2:
        raise ValueError(f"Las columnas y filas de la matriz deben ser 2.")
    
    return A[0][0] * A[1][1] - A[1][0] * A[0][1]

def det(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        matrices = Matriz(A.cortar(1))
    if A.rows == 2:
        return det_2x2(A)
    if A.rows == 1:
        return A.values
    
    suma = 0
    for i in range(A.cols):
        suma += (-1)**(i + 2) * A[0][i] * det(Matriz(matrices[0][i]))
    return suma

def adjunta(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        # Matriz de listas
        matrices = Matriz(A.cortar(A.cols))

    values = []
    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append((-1)**(i + j + 2) * det(Matriz(matrices[i][j])))
        values.append(row)

    return transpuesta(Matriz(values))

def inversa(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    
    d = det(A)
    if d == 0:
        raise ValueError("La matriz no tiene inversa porque el determinante es 0.")
    
    return mult_escalar(adjunta(A), 1 / d)

# Matriz transpuesta
def transpuesta(A):
    values = []

    for i in range(A.cols):
        row = []
        for j in range(A.rows):
            row.append(A[j][i])
        values.append(row)

    return Matriz(values)

# Ejemplos de matrices
A = Matriz([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

B = Matriz([[2, 0, 0, 0], [0, 4, 0, 0], [0, 0, 5, 0], [0, 0, 0, 10]])

C = Matriz((["a", "b", "c", "d"],
            ["e", "f", "g", "h"],
            ["i", "j", "k", "l"],
            ["m", "n", "o", "p"]))

print(mult_matrices(inversa(B), B))