import unittest
from Polynomials import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_get_derivative_1(self):
        f = Polynomial('2x^3+3x+1')
        result = f.get_derivative()
        expected = '6x2+3'
        self.assertEqual(result, expected)

    def test_get_derivative_2(self):
        f = Polynomial('x^4+10*x^3')
        result = f.get_derivative()
        expected = '4x3+30x2'
        self.assertEqual(result, expected)

    def test_get_derivative_3(self):
        f = Polynomial('1+x^2')
        result = f.get_derivative()
        expected = '2x'
        self.assertEqual(result, expected)
    
    def test_get_derivative_4(self):
        f = Polynomial('3x^2')
        result = f.get_derivative()
        expected = '6x'
        self.assertEqual(result, expected)

    def test_get_derivative_of_a_constant(self):
        f = Polynomial('123')
        result = f.get_derivative()
        expected = '0'
        self.assertEqual(result, expected)

    def test_get_derivative_of_x_to_the_power_of_one(self):
        f = Polynomial('2x')
        result = f.get_derivative()
        expected = '2'
        self.assertEqual(result, expected)

    def test_get_derivative_of_1_x(self):
        f = Polynomial('1x')
        result = f.get_derivative()
        expected = '1'
        self.assertEqual(result,expected)
    
    # def test_polynomial_string_version(self):
    #     f = Polynomial('3x^2')
    #     result = str(f)
    #     expected = "The derivative of f(x) = 3x^2 is:\nf'(x) = 6*x"
    #     self.assertEqual(result,expected)
    

if __name__ == "__main__":
    unittest.main()