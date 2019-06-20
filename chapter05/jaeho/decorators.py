import functools
import time

def do_twice(func):
    """Run the decorated function twice"""
    @functools.warps(func)
    def wrapper_do_twice(*args, **kwrags):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value - func(*args, **kwargs)
        end_time  = time.perf_counter()
        run_time = end_time - start_time
        print('Finished {!r} in {:.4f} secs'.format(func.__name__, run_time))
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kawrgs):
        args_repr = [repr(a) for a in args]
        kwrags_repr = ['{}={!r}'.format(k, v) for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwrags_repr)
        print('Calling {}({})'.format(func.__name__, signature))
        value = func(*args, **kwargs)
        print('{} returned {!r}'.format(func.__name__, value))
        return value
    return wrapper_debug
