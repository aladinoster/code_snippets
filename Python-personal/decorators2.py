"""
    Simple example of a tracer decorator
"""


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Trace: calling function ({func.__name__})')
        print(f'with arguments: {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'Trace: function ({func.__name__}) returned {original_result}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


if __name__ == "__main__":
    say('Jane', 'Hello world')
