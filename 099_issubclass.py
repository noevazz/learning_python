"""
Python offers a function which is able to identify a relationship between two classes,
it can check if a particular class is a subclass of any other class. 
"""

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass
print(issubclass(Vehicle, Vehicle))
print(issubclass(LandVehicle, Vehicle))
"""
#↓ is a subclass of → 	Vehicle 	LandVehicle 	TrackedVehicle
#Vehicle 	            True    	False 	        False
#LandVehicle 	        True 	    True 	        False
#TrackedVehicle 	    True 	    True     	    True

"""