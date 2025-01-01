# Write a Python program to create a class representing a Circle. Include methods to calculate its area
# and perimeter.
import math

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r ** 2

def main():
    try:
        r = float(input('Enter circle radius: '))

        if r < 0:
            raise Exception("radius cannot be -ve")
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    circle = Circle(r)
    print(circle.area())

if __name__ == '__main__':
    main()