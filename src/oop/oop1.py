# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# Base/Super class
class Vehicle():
    def __init__(self, maker = "", colour = "", capacity = 0, speed = 0):
        self.maker = maker
        self.colour = colour
        self.capacity = capacity
        self.speed = speed
    
    def accelerate(self):
        pass

    def stop_engine(self):
        pass

# Both FlightVehicle and GoundVehicle are subclasses or children of the Vehicle class
# also they are sibling to each other
class FlightVehicle(Vehicle):
    def __init__(self, maker = "", colour = "", capacity = 0, speed = 0, wings = 2):
        super().__init__(maker, colour, capacity, speed)
        self.wings = wings

    def take_off(self):
        pass

    def land(self):
        pass

class GroundVehicle(Vehicle):
    def __init__(self, maker = "", colour = "", capacity = 0, speed = 0, wheels = 4):
        super().__init__(maker, colour, capacity, speed)
        self.wheels = wheels

# Both Starship and Airplane inherit properties from the FlightVehicle
# which in turn inherits from the Vehicle superclass, 
# they also inherit all the method of the parent and granparent componentss
# but they can also override them if needed 
class Starship(FlightVehicle):
    def __init__(self, maker, colour, capacity, speed, wings, engine = "propulsor"):
        super().__init__(maker, colour, capacity, speed, wings)
        self.engine = engine

class Airplane(FlightVehicle):
    def __init__(self, maker, colour, capacity, speed, wings):
        super().__init__(maker, colour, capacity, speed, wings)

# Both Car a Motorcycle are subclasses of the GroundVehicle parent class and the Vehicle Granparent base class which they inherit all the properties and methods from
class Car(GroundVehicle):
    def __init__(self, maker, colour, capacity, speed, wheels = 4):
        super().__init__(maker, colour, capacity, speed, wheels)

class Motorcycle(GroundVehicle):
    def __init__(self, maker, colour, capacity, speed, wheels = 2):
        super().__init__(maker, colour, capacity, speed, wheels)