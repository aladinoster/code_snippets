import functools


def noop(f):
    @functools.wraps(f)  # Keep __name__, doc
    def noop_wrapper():
        return f()

    # copying metadata from f
    # noop_wrapper.__name__ = f.__name__
    # noop_wrapper.__doc__ = f.__doc__

    return noop_wrapper


@noop
def hello():
    " Known message"
    print("Hello world!")


hello()
print(hello.__name__)
print(hello.__doc__)
