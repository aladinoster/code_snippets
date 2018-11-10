"""
Show how can you wrap functions in modules without changing names
"""

from decorators3 import hello

hello('Pedro')
hello('Pablo')
print(hello.count)
