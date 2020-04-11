import unittest
from unittest.mock import patch
from os.path import isdir,isfile
from book_reader import book_reader


class TestBookReader(unittest.TestCase):
    @patch('builtins.input', return_value = ' ')
    def test_book_reader_extracts_files(self, mock_input):
        book_reader('Book.zip')

        self.assertTrue(isdir('./book'))
        self.assertTrue(isfile('./book/001.txt'))
        self.assertTrue(isfile('./book/002.txt'))

    @patch('builtins.input', return_value = ' ')
    def test_book_reader_reads_all_chapters(self, mock_input):
        times = book_reader('Book.zip')

        self.assertEqual(times, 10)



        

if __name__ == "__main__":
    unittest.main()
