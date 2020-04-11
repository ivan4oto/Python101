import unittest
from os import remove
from os.path import isdir, isfile
from book_generator import book_generator


class TestBookGenerator(unittest.TestCase):
    def test_bookgenerator_makes_bookfile(self):
        book_generator(5, 50)
        
        self.assertTrue(isfile('newly_generated_book.txt'))
        remove('newly_generated_book.txt')

    #test may lag if too large book if generated
    def test_book_has_chapters(self):
        book_generator(5, 50)
        result = 0
        with open('newly_generated_book.txt') as file:
            for line in file:
                result += line.count('# Chapter')
        
        self.assertEqual(result, 5)
        remove('newly_generated_book.txt')
if __name__ == "__main__":
    unittest.main()