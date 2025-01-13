# Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
# methods start() and stop(). The Car class should have instances of Engine and Wheel classes
# as attributes. Implement a method start_car() in the Car class which starts the engine and prints
# "Car started".

class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} Engine started")

    def stop():
        print("Engine stoped")

class Wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} Wheel started")

    def stop():
        print("Wheel stoped")

class Car:
    def __init__(self, engine, wheel):
        self.engine = engine
        self.wheel = wheel
    
    def start_car(self):
        self.engine.start()
        print("Car started")


def main():
    e = Engine("Disel")
    w = Wheel("MRF")
    c = Car(e, w)
    c.start_car()

if __name__ == "__main__":
    main()