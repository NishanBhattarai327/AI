# Define a class Vehicle with attributes make and model, and a method drive() which prints
# "Driving the [make] [model]". Then, create a subclass Car that inherits from Vehicle and overrides
# the drive() method to print "Driving the [make] [model] car".

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f'Driving the {self.make} {self.model}')

class Car(Vehicle):
    def drive(self):
        print(f'Driving the {self.make} {self.model} car')

def main():
    make = 'Toyota'
    model = 'Corolla'
    car = Car(make, model)
    car.drive()
    vec = Vehicle(make, model)
    vec.drive()

if __name__ == '__main__':
    main()