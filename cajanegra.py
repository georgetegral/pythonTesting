import unittest

def suma(n1,n2):
    return n1+n2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        n1 = 10
        n2 = 5

        resultado = suma(n1,n2)
        self.assertEqual(resultado,15)

    def test_suma_dos_negativos(self):
        n1 = -10
        n2 = -7

        resultado = suma(n1,n2)
        self.assertEqual(resultado, -17)

if __name__ == "__main__":
    unittest.main()