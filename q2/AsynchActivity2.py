# What is duck typing? Duck typing is another way to achieve polymorphism besides Inheritance.
#                       Object must have the minimun necessary attributes/methods
#                       "If it looks like a duck and quacks like a duck, then it must be a duck"

# What did the Car class need to have so it could work inside the same loop as Dog and
# Cat, even if it does not inherit from the Animal class?
# -it had to implement the minimum necessary attributes and methods that the loop expected
# -define speak() method and alive attribute

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
        vehicle.move()

vehicles = [Car(), Boat(), Drone()]

for vehicle in vehicles:
    start_trip(vehicle)

# how does this code demonstrate polymorphism?
# - this code demonstrates polymorphism because the start_trip function can accept any object that has a move() method, regardless of its class. 