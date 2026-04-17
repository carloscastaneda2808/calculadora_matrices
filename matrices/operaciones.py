from matriz import Matriz

def suma(A, B):
    if A.cols != B.cols or A.rows != B.rows:
        raise IndexError(f"Las matrices no son del mismo tamaño")
    
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j] + B[i][j])
        values.append(row)

    return Matriz(values)

def resta(A, B):
    if A.cols != B.cols or A.rows != B.rows:
        raise IndexError(f"Las matrices no son del mismo tamaño")
    
    values = []

    for i in range(A.rows):
        row = []
        for j in range(A.cols):
            row.append(A[i][j] - B[i][j])
        values.append(row)

    return Matriz(values)
    

A = Matriz([[1, 2, 3], [4, 5, 6]])
B = Matriz([[7, 8, 9], [10, 11, 12]])
print(resta(A, B).values)