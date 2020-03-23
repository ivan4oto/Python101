import unittest
from fractionsOOP import Fractions
from fractions import Fraction

class TestFractionsClass(unittest.TestCase):
    def test_get_fractions(self):
        fractsList = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        fracts = Fractions(fractsList)
        result = fracts.get_fractions()

        self.assertEqual(result, fractsList)

    def test_sort_fractions(self):
        fracts = Fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
        fracts.sort_fractions()
        result = fracts.get_fractions()
        sortedfracts = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

        self.assertEqual(result, sortedfracts)
    
    def test_collect_fractions(self):
        fractsList = [(5, 6), (4,2)]
        fractsSum = (17,6)
        fracts = Fractions(fractsList)
        result = fracts.sum_fractions()        

        self.assertEqual(result, fractsSum)

    

if __name__ == "__main__":
    unittest.main()