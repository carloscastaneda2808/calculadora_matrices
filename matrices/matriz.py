
class Matriz:
    def __init__(self, values):
        # Verifica si cada fila tiene el mismo nummero de elementos
        cols = None

        for row in values:
            if cols == None:
                cols = len(row)
            elif cols != len(row):
                raise ValueError("La matriz debe tener las mismas columnas en cada fila!")
            
        if cols == 0:
            raise ValueError("Las filas deben tener al menos una columna")
            
        self.cols = cols
        self.rows = len(values)
        self.values = values

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.rows:
            raise IndexError(f"Indice para fila fuera de rango! ({idx})")
        
        return self.values[idx]

a = Matriz([[1, 2, 3], [4, 5, 6]])

a[5][2]
