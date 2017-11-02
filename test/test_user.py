import unittest
import user

class UserTest(unittest.TestCase):

    def testSaludarDeberiaDevolverHola(self):
        #AAA
        #ARRANGE
        saludoEsperado = "Hola"

        #ACT
        saludoRecibido = user.saludar()

        #ASSERT
        self.assertEqual(saludoEsperado, saludoRecibido)