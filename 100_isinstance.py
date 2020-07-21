class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()

print(isinstance(myVehicle, Vehicle))
print(isinstance(myLandVehicle, Vehicle))
print(isinstance(myLandVehicle, TrackedVehicle))
"""
↓ is instance of →   	Vehicle 	LandVehicle 	TrackedVehicle
myVehicle 	            True    	False 	        False
myLandVehicle 	        True 	    True 	        False
myTrackedVehicle        True 	    True     	    True
"""