class Car:
    """ Vehicle class
    Example on how to create __repr__ , __str__
    methods to provide useful information about 
    your classess
    """

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}' +
                f'({self.color!r}, {self.mileage!r})')

    def __str__(self):
        return (f'A {self.color} car')


if __name__ == "__main__":
    my_car = Car('blue', 13)
    print(my_car)
