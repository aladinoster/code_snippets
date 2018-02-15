# Decorators examples

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('This wrapper was executed before:  {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('This call method was executed before:  {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_function
def display_function():
    print('Esto es la function display')


@decorator_function
def display_info(name, age):
    print('Instead we display: He is {} and he is {}'.format(name, age))


@decorator_class
def display_sum(n1, n2):
    print('Instead the sum of {} and {} is {}'.format(n1, n2, n1 + n2))

# Equivalent to say
# display_function = decorator_function(display_function)
# display_info = decorator_function(display_info)

# Double decorators! This is to apply double wrapping (High stuff!)


from functools import wraps


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_function.__name__, t2))
        return result

    return wrapper


import time

# Important: the following decorator is equivalent to display_nombre = my_logger(my_timer(display_nombre))

@my_logger
@my_timer
def display_nombre(nombre, apellido):
    time.sleep(1)
    print('Yo me llamo {} {}'.format(nombre, apellido))

display_nombre('Andres', 'Ladino')
display_info('Andres', 31)