from fractions import Fraction

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
    
    def cortar(self, nivel_row):
        values2 = []
        for i in range(nivel_row):
            row2 = []
            for j in range(self.cols):
                values = []
                for k in range(self.rows):
                    row = []
                    for l in range(self.cols):
                        if i != k and j != l:
                            row.append(self[k][l])
                    if len(row) != 0:
                        values.append(row)
                row2.append(values)
            values2.append(row2)

        # Las matrices se devuelven como una lista de listas
        return values2
        
    def __str__(self):
        self_as_str = ""

        for i in range(self.rows):
            self_as_str += "["
            for j in range(self.cols):
                self_as_str += f"{Fraction(self[i][j]).limit_denominator(10):>5}, "

            if self_as_str.endswith(', '):
                self_as_str = self_as_str[0 : -2]
            self_as_str += "]\n"

        #if self_as_str.endswith('\n'):
        #        self_as_str = self_as_str[0 : -1]

        return self_as_str