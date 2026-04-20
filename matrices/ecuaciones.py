from math import sqrt

class Polinomio:
    def __init__(self, coeficientes = [], variables = []):
        if coeficientes != []:
            self.operaciones = len(coeficientes)
        else:
            self.operaciones = 0

        self.coeficientes = coeficientes
        self.variables = variables

    def agregar(self, coeficientes, variables):
        self.coeficientes.append(coeficientes)
        self.operaciones += 1
        self.variables.append(variables)



    def suma_variables0(self):
        if self.variables == []:
            suma = 0
            for i in self.coeficientes:
                suma += i

        return Polinomio([suma])
    
    def suma(self):
        suma = Polinomio(self.coeficientes, self.variables)

        print(suma.coeficientes)
        print(suma.variables)
        for i in range(self.operaciones):
            for j in range(i, self.operaciones):
                if self.variables[i] == self.variables[j] and i != j:
                    print(self)
                    suma.coeficientes.remove(self.coeficientes[i])
                    suma.coeficientes.remove(self.coeficientes[j])
                    suma.variables.remove(self.variables[i])
                    print(self)
                    suma.coeficientes.insert(i, self.coeficientes[i] + self.coeficientes[j])
                    suma.variables.insert(j, self.variables[i])
                    suma.operaciones -= 1
        
        return suma
                    

    def __str__(self):
        self_as_str = ""

        for i in range(self.operaciones):
            if self.coeficientes != []:
                if self.coeficientes[i] >= 0:
                    self_as_str += f"+{self.coeficientes[i]}"
                else:
                    self_as_str += f"{self.coeficientes[i]}"
            
            if self.variables != []:
                self_as_str += f"{self.variables[i]}"


        return self_as_str

def ecuacion(a, b, c, y):
    x = 0
    while a * x**2 + b * x + c != y:
        if a * x**2 + b * x + c < y:
            x += 1
        else:
            x -= 1
    
    return x

print(ecuacion(0, 1, 4, 0))
        
#ecuacion1 = Polinomio([5, 4, 6, 3], ["x", "y", "x", "y"])
#print(ecuacion1.suma())