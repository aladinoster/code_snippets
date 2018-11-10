class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


# In this case we create an instance to decorate
tracer = Trace()


@tracer
def sum(a, b):
    return print(a+b)


sum(3, 5)
tracer.enabled = False
sum(3, 5)
