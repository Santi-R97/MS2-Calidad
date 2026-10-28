import unittest
from calculadora import calcular_total


class TestCalculadora(unittest.TestCase):

    def test_calcular_total_con_descuento(self):
        # Arrange
        precio = 1000
        descuento = 20

        # Act
        resultado = calcular_total(precio, descuento)

        # Assert
        self.assertEqual(resultado, 800)

    def test_calcular_total_sin_descuento(self):
        # Arrange
        precio = 500
        descuento = 0

        # Act
        resultado = calcular_total(precio, descuento)

        # Assert
        self.assertEqual(resultado, 500)

    def test_descuento_invalido(self):
        # Arrange
        precio = 1000
        descuento = 120

        # Act + Assert
        with self.assertRaises(ValueError):
            calcular_total(precio, descuento)


if __name__ == "__main__":
    unittest.main()
