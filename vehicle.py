class Vehicle:
    def __init__(self, make, color):
        self.make = make
        self.color = color

    def accelerate(self):
        print("Acceleration starts")

    def honk(self):
        print("Honk Honk")


class Bus(Vehicle):
    def __init__(self, color, make, passengers):
        super().__init__(make, color)
        self.passengers = passengers

    def start_boarding(self):
        print("The bus is boarding")


class Lorry(Vehicle):
    def __init__(self, make, color, max_load):
        super().__init__(make, color)
        self.max_load = max_load

    def unload(self):
        print("Unloading")


