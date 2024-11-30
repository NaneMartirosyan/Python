from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type

    def honk(self):
        return f"The {self.name} honks: Beep Beep!"

class RaceCar(Car):
    def __init__(self, name, speed, fuel_type, sponsor):
        super().__init__(name, speed, fuel_type)
        self.sponsor = sponsor

    def race(self):
        return f"The {self.name} sponsored by {self.sponsor} is racing at {self.speed} km/h!"

class Plane(Vehicle):
    def __init__(self, name, speed, airline):
        super().__init__(name, speed)
        self.airline = airline

    def fly(self):
        return f"The {self.name} from {self.airline} is flying at {self.speed} km/h."

class Boat(Vehicle):
    def __init__(self, name, speed, boat_type):
        super().__init__(name, speed)
        self.boat_type = boat_type

    def sail(self):
        return f"The {self.name} ({self.boat_type}) is sailing at {self.speed} km/h."

def main():
    car = Car("Sedan", 120, "Gasoline")
    race_car = RaceCar("Formula 1", 300, "Gasoline", "Red Bull")
    plane = Plane("Boeing 747", 900, "Delta Airlines")
    boat = Boat("Yacht", 50, "Luxury")

    print(car.move())
    print(car.honk())
    print(race_car.move())
    print(race_car.race())
    print(plane.move())
    print(plane.fly())
    print(boat.move())
    print(boat.sail())

if __name__ == "__main__":
    main()

