class Calculadora:

    def add(self, a, b):
        return a + b
    def resta(self, a, b):
        return a - b
    def multiplicacion(self, a, b):
        return a * b    
    def division(self, a, b):
        if b == 0:
            return "error"
        else:
            return a / b
    def sqrt(self, n):
        if n < 0:
            return "error"
        x = n /2

        while True:
            if x * x == n:
                return x
            else:
                copia_x = x
                x = (x + (n/x)) / 2
            if copia_x == x:
                break
        return x   