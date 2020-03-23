import unittest
from fractions import Fraction
from fractions_task import simplify_fraction, collect_fractions, sort_fractions


class TestSimplifyFraction(unittest.TestCase):
    def test_for_4_and_10(self):
        result = simplify_fraction(4,10)
        self.assertEqual(result, (2,5))
    def test_with_462_and_63(self):
        result = simplify_fraction(462,63)
        self.assertEqual(result, (22,3))



class TestCollectFractions(unittest.TestCase):
    def test_sum_two_fractions(self):
        fractsList = [(1, 4), (1, 2)]
        x = Fraction(1,4) + Fraction(1,2)
        result = (x.numerator, x.denominator)
        testresult = collect_fractions(fractsList)
        self.assertEqual(result, testresult)

    def test_sum_more_than_two_fractions(self):
        fractList = [(1,4),(1,2),(1,5)]
        x = Fraction(1,4) + Fraction(1,2) + Fraction(1,5)
        result = (x.numerator, x.denominator)
        testresult = collect_fractions(fractList)
        self.assertEqual(result, testresult)
    
    def test_single_fraction_input(self):
        fractList = [(2,8)]
        x = (1,4)
        testresult = collect_fractions(fractList)
        self.assertEqual(x, testresult)


class TestSortFractions(unittest.TestCase):
    def test_ascending_order_sort(self):
        unsorted = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        expected = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        result = sort_fractions(unsorted)
        self.assertEqual(result, expected)
    def test_descending_order_sort(self):
        unsorted = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        expected = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        result = sort_fractions(unsorted, ascending = False)
        self.assertEqual(result, expected[::-1])

if __name__ == "__main__":
    unittest.main()