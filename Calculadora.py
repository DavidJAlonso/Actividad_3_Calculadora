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