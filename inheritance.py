class vheicle:

    def _init_(self,name,max_speed, mileage):
        self.name=name
        self.max_speed= max_speed
        self.mileage= mileage

class Bus(vheicle):
            pass
school_bus = Bus("School Volvo",180 12)
print("Vheicle name:", School_bus.name, "speed:", school_bus.max_speed, "Mileage:", School_bus.mileage)
