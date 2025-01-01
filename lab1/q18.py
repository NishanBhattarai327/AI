# Implement a class Shape with a method area() which returns 0. Then, create subclasses
# Rectangle and Circle. Overload the area() method in both subclasses to calculate and return
# the area of a rectangle and a circle respectively.

import math

class Shape:
    def __init__(self, dim):
        self.dimension = dim
        print(dim)
    
    def area():
        return 0

class Rectangle(Shape):
    def area(self):
        return self.dimension['length'] * self.dimension['bredth']

class Circle(Shape):
    def area(self):
        return math.pi * self.dimension['radius'] ** 2

def main():
   c = Circle({'radius': 45})
   print(c.area())

   r = Rectangle({'length': 10, 'bredth': 20})
   print(r.area())

if __name__ == '__main__':
    main()