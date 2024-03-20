class Vehicle:
    def __init__(self, name: str, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity: int):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    pass

School_bus = Bus()