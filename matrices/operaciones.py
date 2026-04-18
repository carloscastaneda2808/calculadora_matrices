from matriz import Matriz

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

def mult_escalar(A, escalar):
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j] * escalar)
        values.append(row)

    return Matriz(values)

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

def det_2x2(A):
    if A.rows!= 2 and A.cols != 2:
        raise ValueError(f"Las columnas y filas de la matriz deben ser 2.")
    
    return A[0][0] * A[1][1] - A[1][0] * A[0][1]

def sarrus(A):
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j])

        for j in range(A.cols - 1):
            row.append(A[i][j])

        values.append(row)

    return Matriz(values)

def det_3x3(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    
    B = sarrus(A)

    suma = 0
    for i in range(A.cols):
        mul = 1
        for j in range(B.rows):
            mul *= B[0 + j][i + j]
        suma += mul

    resta = 0
    for i in range(B.cols - 1, A.cols - 2, -1):
        mul = 1
        for j in range(B.rows):
            mul *= B[0 + j][i - j]
        resta -= mul

    return suma + resta

def cortar(A):
    matrices = []
    for i in range(A.cols):
        values = []
        for j in range(A.rows):
            row = []
            for k in range(A.cols):
                if 0 != j and i != k:
                    row.append(A[j][k])
            
            if len(row) != 0:
                values.append(row)

        matrices.append(Matriz(values))
    return matrices

def det(A):
    if A.rows != A.cols:
        raise ValueError(f"La matriz debe ser cuadrada.")
    if A.rows > 2:
        matrices = cortar(A)
    if A.rows == 2:
        return det_2x2(A)
    if A.rows == 1:
        return A.values
    
    suma = 0
    for i in range(A.cols):
        suma += (-1)**(i + 2) * A[0][i] * det(matrices[i])
    return suma

def transpuesta(A):
    values = []

    for i in range(A.cols):
        row = []
        for j in range(A.rows):
            row.append(A[j][i])
        values.append(row)

    return Matriz(values)

A = Matriz([[3, 1, 2],
            [2, 1, 1],
            [1, 0, 1]])

B = Matriz([[7, 8], 
            [9, 10], 
            [11, 12]])

print(det(A))