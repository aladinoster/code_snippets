"""
    Simple example of a tracer decorator
"""
from functools import wraps


def trace(func):
    @wraps(func)  # Decorator to keep metadata __doc__ i.e  Important line!!
    def wrapper(*args, **kwargs):
        print(f'Trace: calling function ({func.__name__})')
        print(f'with arguments: {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'Trace: function ({func.__name__}) returned {original_result}')
        return original_result
    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result
    return wrapper


def print_doc(func):
    def wrapper(*args, **kwargs):
        print(f'Documentation for function ({func.__name__}):')
        print(f'{func.__doc__}')
        return func(*args, **kwargs)
    return wrapper


@print_doc
@trace
def say(name, line):
    """ This documentation was important """
    return f'{name}: {line}'


@print_doc
@my_timer
def saybark(name, line):
    """ This documentation was important """
    return f'{name}!: {line}!'.upper()


if __name__ == "__main__":
    say('Jane', 'Hello world')
    # None eh! Not using functools forgets metadata!
    saybark('Jane', 'Hello world')
