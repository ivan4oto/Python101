import unittest
import os
from decorators import accepts, performance

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
    def test_performance_writes_for_each_call(self):
        @performance('text_test.txt')
        def return_hi(h):
            return h
        
        return_hi('hi')


        self.assertTrue(os.path.isfile('text_test.txt'))
        os.remove("text_test.txt")









if __name__ == "__main__":
    unittest.main()