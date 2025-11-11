class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclass sould be implement this.")
class Car(Vehicle):
    def drive(self):
        print("driving a car")
class Bicycle(Vehicle):
    def drive(self):
        print("riding a bicycle")

class Hoverboard:
    def drive(self):
        print("hovering a hoverboard")

class Boat(Vehicle):
    def sail(self):
        print("Sailing a boat")

# polymorphic method
def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} can't be driven")

def main():
    my_car = Car()
    my_bicycle = Bicycle()
    my_hoverboard = Hoverboard()
    my_boat = Boat()

    drive_vehicle(my_car)
    drive_vehicle(my_bicycle)
    drive_vehicle(my_hoverboard)
    drive_vehicle(my_boat)

if __name__ == "__main__":
    main()