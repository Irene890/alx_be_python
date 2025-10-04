import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.add(self,10,5),15)
        self.assertEqual(SimpleCalculator.add(self,-1,1),0)
    
    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(self,10,5),5)
        
    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(self,10,5),50)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(self,10,5),2)
