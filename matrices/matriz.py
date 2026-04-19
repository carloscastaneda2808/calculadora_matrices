
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
        
    def __setitem__(self, idx, row):
        if idx < 0 or idx >= self.rows:
            raise IndexError(f"Indice para fila fuera de rango! ({idx})")
        
        if len(row) != self.cols:
            raise ValueError(f"La longitud de la fila esta fuera de rango!")

        self.values[idx] = row

    def set_item(self, col_idx, row_idx, item):
        if col_idx < 0 or col_idx >= self.cols:
            raise IndexError(f"Indice para columna fuera de rango! ({col_idx})")
        if row_idx < 0 or row_idx >= self.rows:
            raise IndexError(f"Indice para fila fuera de rango! ({row_idx})")
        
        self.values[row_idx][col_idx] = item

    def __str__(self):
        self_as_str = ""

        for i in range(self.rows):
            self_as_str += "["
            for j in range(self.cols):
                self_as_str += f"{self[i][j]}, "

            if self_as_str.endswith(', '):
                self_as_str = self_as_str[0 : -2]
            self_as_str += "]\n"

        if self_as_str.endswith('\n'):
                self_as_str = self_as_str[0 : -1]

        return self_as_str
