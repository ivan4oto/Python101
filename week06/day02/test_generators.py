import unittest
from generators import chain, compress, cycle


class TestChainGenerator(unittest.TestCase):
    def test_chain_chains_two_different_types(self):
        testgenerator = chain(range(0,6), [6,7,8,9,10])
        result = list(testgenerator)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        self.assertEqual(result, expected)

class TestCompressGenerator(unittest.TestCase):
    def test_compress_returns_correct_values(self):
        boolist = [False, True, True, False, False]
        tocompress = ['Dragan', 'Ivan', 'Petkan', 'Kondio', 'Sandokan']
        x = compress(tocompress, boolist)

        self.assertEqual(list(x), ['Ivan', 'Petkan'])

    def test_compress_works_with_range(self):
        boolist = [False, True, True, False, False]
        tocompress = range(1,6)
        y = compress(tocompress, boolist)

        self.assertEqual(list(y), [2, 3])

class TestCyleGenerator(unittest.TestCase):
    def test_cycle_continues_after_end_of_given_list(self):
        x = cycle([1,2,3])
        result = []
        for i in range(5):
            result.append(next(x))

        self.assertEqual(result, [1,2,3,1,2])



if __name__ == "__main__":
    unittest.main()
