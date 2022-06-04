from cmath import sqrt
import unittest
from Calculadora import Calculadora

a = -1000
b = -1000
class CalculadoraTest(unittest.TestCase):
    calculadora = Calculadora()
    
    for a in range (1000):
        for b in range (1000):
    
            def test_suma(self):
                self.assertEqual(a+b, self.calculadora.add(a,b))
            def test_resta(self):
                self.assertEqual(a-b, self.calculadora.resta(a,b))
            def test_multiplicacion(self):
                self.assertEqual(a*b, self.calculadora.multiplicacion(a,b))
            def test_division(self):
                if (b == 0):
                    self.assertEqual("error", self.calculadora.division(a,b))
                else:
                    self.assertEqual(a/b, self.calculadora.division(a,b))
            def test_sqrt(self):
                if (a < 0):
                    self.assertEqual("error", self.calculadora.sqrt(a))
                else:
                    self.assertEqual(sqrt(a), self.calculadora.sqrt(a))
                
    
if __name__ == "__main__":
    unittest.main()


    