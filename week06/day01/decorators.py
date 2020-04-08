import time
from decimal import Decimal

def accepts(*types):
    def decorator(function):
        def wrapper(*args):
            for i in range(len(args)):
                if type(args[i]) != types[i]:
                    raise ValueError(f'"{args[i]}" must be of type {types[i]}') 
            return function(*args)
        return wrapper
    return decorator

def performance(file_name):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = time.time()
            file1 = open(file_name,"a")
            retval = function(*args, **kwargs)
            file1.write(f'It took us {Decimal(time.time()-start)} seconds to run this.\n')
            file1.close()
            return retval
        return wrapper
    return decorator

def silence(file_name):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                function(*args, *kwargs)
            except Exception as e:
                file1 = open(file_name, "a")
                file1.write(f"Calling {function.__name__} raised an error - '{type(e).__name__}' - {e}. With arguments --> {*args, *kwargs}\n")
                file1.close()
            return function(*args, *kwargs)
        return wrapper
    return decorator
