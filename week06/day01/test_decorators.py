import unittest
import os
from decorators import accepts, performance, silence

class TestAccept(unittest.TestCase):    
    def test_accept_raises_error_one_argument(self):
        @accepts(int)
        def result(a):
            return a

        with self.assertRaises(Exception) as context:
            result("a")

        self.assertTrue('"a" must be of type <class \'int\'>' in str(context.exception))


    def test_accept_raises_no_errors(self):
        @accepts(int, str, list)
        def result(a,b,c):
            return c,b,a

        try:
            result(1, 'a',[1, '2', True, False])
        except ValueError:
            self.fail("This should not raise an error dude... ")

class TestPerformance(unittest.TestCase):
    def test_performance_creates_log(self):
        @performance('text_test.txt')
        def return_hi(a,b):
            return a+b
        
        return_hi(1,2)

        self.assertTrue(os.path.isfile('text_test.txt'))
        os.remove("text_test.txt")

    def test_performance_write_new_line_each_time(self):
        @performance('text_testlines.txt')
        def return_hi(a,b):
            return a + b

        @performance('text_testlines.txt')
        def saybye(s):
            print(s)

        return_hi(1,2)
        saybye('bye')
        with open('text_testlines.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(len(lines), 2)
        os.remove("text_testlines.txt")


class TestSilence(unittest.TestCase):
    def test_silence_logs_type_error(self):
        @silence('errors.txt')
        def returnsum(a,b):
            return a+b
        try:
            returnsum('a', 2)
        except Exception:
            pass

        expectedline = "Calling returnsum raised an error - 'TypeError' - must be str, not int. With arguments --> ('a', 2)"
        with open('errors.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(expectedline, lines[0])
        self.assertTrue(os.path.isfile('errors.txt'))
        os.remove('errors.txt')

    def test_silence_does_nothing_if_no_error(self):
        @silence('errors2.txt')
        def sumtwo(a,b):
            return a+b
        
        try:
            sumtwo(1,2)
        except Exception:
            pass

        self.assertFalse(os.path.isfile('errors2.txt'))
        
        








if __name__ == "__main__":
    unittest.main()