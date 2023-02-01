import unittest
class TestCalculadora(unittest.TestCase):
	def test_2_mas_2(self):
	calc=Calculadora()
	self.asserEquals(4,calc.sumar(2,2))