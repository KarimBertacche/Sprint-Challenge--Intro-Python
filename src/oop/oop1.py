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

