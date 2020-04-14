import unittest
from decimal import Decimal
from time import sleep
import io
import sys
from context_managers import silence_exception, SilenceException, ChangePrecision, change_precision, MeasurePerformance, measure_performance

# Marto's tests ................................................
class SilenceExceptionTests(unittest.TestCase):
    def test_silences_passed_exception(self):
        exception = None

        try:
            with silence_exception(ValueError):
                raise ValueError('Testing.')
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_different_exception_from_passed_one(self):
        with self.assertRaises(ValueError):
            with silence_exception(TypeError):
                raise ValueError('Testing.')

    def test_not_silences_passed_exception_outside_context_manager(self):
        with self.assertRaises(ValueError, msg='Testing outside with-block'):
            with silence_exception(ValueError):
                raise ValueError('Testing inside with-block')

            raise ValueError('Testing outside with-block')

    def test_silences_passed_exception_with_correct_message(self):
        exception = None
        exc_message = 'Testing with msg argument.'

        try:
            with silence_exception(ValueError, msg=exc_message):
                raise ValueError(exc_message)
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_passed_exception_with_different_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(ValueError):
            with silence_exception(ValueError, msg=exc_message):
                raise ValueError(f'{exc_message} - different.')

    def test_not_silences_different_exception_with_same_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(TypeError):
            with silence_exception(ValueError, msg=exc_message):
                raise TypeError(exc_message)


class SilenceExceptionClassTests(unittest.TestCase):
    def test_silences_passed_exception(self):
        exception = None

        try:
            with SilenceException(ValueError):
                raise ValueError('Testing.')
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_different_exception_from_passed_one(self):
        with self.assertRaises(ValueError):
            with SilenceException(TypeError):
                raise ValueError('Testing.')

    def test_not_silences_passed_exception_outside_context_manager(self):
        with self.assertRaises(ValueError, msg='Testing outside with-block'):
            with SilenceException(ValueError):
                raise ValueError('Testing inside with-block')

            raise ValueError('Testing outside with-block')

    def test_silences_passed_exception_with_correct_message(self):
        exception = None
        exc_message = 'Testing with msg argument.'

        try:
            with SilenceException(ValueError, msg=exc_message):
                raise ValueError(exc_message)
        except Exception as exc:
            exception = exc

        self.assertIsNone(exception)

    def test_not_silences_passed_exception_with_different_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(ValueError):
            with SilenceException(ValueError, msg=exc_message):
                raise ValueError(f'{exc_message} - different.')

    def test_not_silences_different_exception_with_same_message(self):
        exc_message = 'Testing with msg argument.'

        with self.assertRaises(TypeError):
            with SilenceException(ValueError, msg=exc_message):
                raise TypeError(exc_message)
#End of Marto's tests ................................................

class ChangePrecisionClassTests(unittest.TestCase):
    def test_change_precision_class_changes_precision(self):
        result = 0
        with ChangePrecision(2):
            result = Decimal('1.123132132') + Decimal('2.23232')
        self.assertEqual(str(result), '3.4')

    def test_ChangePrecision_class_outside_block(self):
        with ChangePrecision(2):
            Decimal('1.123132132') + Decimal('2.23232')
        result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(str(result), '3.355452132')

class ChangePrecisionFuncTests(unittest.TestCase):
    def test_change_precision_class_changes_precision(self):
        result = 0
        with change_precision(2):
            result = Decimal('1.123132132') + Decimal('2.23232')
        self.assertEqual(str(result), '3.4')

    def test_ChangePrecision_class_outside_block(self):
        with change_precision(2):
            Decimal('1.123132132') + Decimal('2.23232')
        result = Decimal('1.123132132') + Decimal('2.23232')

        self.assertEqual(str(result), '3.355452132')

class MeasurePerfomanceClassTests(unittest.TestCase):
    def test_measure_performance_returns_correct_value(self):        
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        with MeasurePerformance():
            sleep(1)
            x = 1+2
            sleep(1)
        result = str(capturedOutput.getvalue())[0]
        sys.stdout = sys.__stdout__

        self.assertEqual(result, '2')

class MeasurePerfomanceFuncTests(unittest.TestCase):
    def test_measure_performance_returns_correct_value(self):        
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        with measure_performance():
            sleep(1)
            x = 1+2
            sleep(1)
        result = str(capturedOutput.getvalue())[0]
        sys.stdout = sys.__stdout__

        self.assertEqual(result, '2')


if __name__ == '__main__':
    unittest.main()