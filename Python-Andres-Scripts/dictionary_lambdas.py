# How to merge two dictionaries
# in Python 3.5+:

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

# Why Python Is Great:
# Function argument unpacking


def myfunc(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)


myfunc(**dict_vec)

# The lambda keyword in Python provides a
# shortcut for declaring small and
# anonymous functions:


def add(x, y): return x + y


add(5, 3)


# You could declare the same add()
# function with the def keyword:

def add(x, y):
    return x + y


add(5, 3)

# So what's the big fuss about?
# Lambdas are *function expressions*:
(lambda x, y: x + y)(5, 3)

# → Lambda functions are single-expression
# functions that are not necessarily bound
# to a name (they can be anonymous).

# → Lambda functions can't use regular
# Python statements and always include an
# implicit `return` statement.
