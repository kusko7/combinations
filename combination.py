class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is driving on the road.")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is sailing on water.")

class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is flying in the sky.")

def demonstrate_movement(vehicle):
    print(f"Demonstrating movement for {vehicle.__class__.__name__}:")
    vehicle.move()
    print("-" * 50)

if __name__ == "__main__":
    # Creating instances of each vehicle
    car = Car("Toyota", "Corolla")
    boat = Boat("Yamaha", "242X")
    plane = Plane("Boeing", "747")

    # Demonstrating polymorphism
    for vehicle in [car, boat, plane]:
        demonstrate_movement(vehicle)
