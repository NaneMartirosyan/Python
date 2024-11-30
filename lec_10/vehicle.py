class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        return f"The {self.name} moves at a speed of {self.speed} km/h."

