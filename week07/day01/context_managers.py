from contextlib import contextmanager
from decimal import getcontext, MAX_PREC, Decimal
from time import time, sleep

class SilenceException:
    def __init__(self, exc_type, msg=None):
        self.exc_type = exc_type
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        same_exception_type = self.exc_type == exc_type
        correct_message = self.msg is None or str(exc_value) == self.msg

        return same_exception_type and correct_message

@contextmanager
def silence_exception(exc_type, msg=None):
    try:
        yield
    except exc_type as exc:
        if msg is not None and str(exc) != msg:
            raise exc

class ChangePrecision:
    def __init__(self, precision):
        self.precision = precision

    def __enter__(self):
        getcontext().prec = self.precision
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = MAX_PREC

@contextmanager
def change_precision(precision):
    try:
        getcontext().prec = precision
        yield
    except Exception:
        pass
    finally:
        getcontext().prec = MAX_PREC

class MeasurePerformance:
    def __init__(self):
        self.bmarks = 0
        self.starttime = time()
        pass

    def __enter__(self):
        return self

    def benchmark(self, msg = None, restart = False):
        self.bmarks += 1
        if msg == None:
            print(f'Benchmark No. {self.bmarks}: {Decimal(time() - self.starttime)}')
        elif msg != None:
            print(f'{msg}: {Decimal(time() - self.starttime)}')
        if restart:
            self.starttime = time()
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'Finished for: {Decimal(time() - self.starttime)}')

def main():
    pass

if __name__ == "__main__":
    main()