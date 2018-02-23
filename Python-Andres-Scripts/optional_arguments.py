def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

# * args collect positional arguments in tuples
# ** kwargs collect keyword arguments in a dictionary


if __name__ == "__main__":
    foo('hello')
    foo('hello', 1, 2, 3)
    foo('hello', 1, 2, 3, key='value', key2=99)
