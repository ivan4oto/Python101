import time

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
    start = time.time()
    file1 = open(file_name,"a")
    def decorator(function):
        def wrapper(*args, **kwargs):
            retval = function(*args, **kwargs)
            file1.write(f'It took us {time.time()-start} seconds to run this.\n')
            file1.close()
            return retval
        return wrapper
    return decorator



