class vehicle:
    def __init__(self, max_speed, milaeage):
        self.max_speed= max_speed
        self.milaeage=milaeage

modelx = vehicle(200,6)
print("Model max speed: ", modelx.max_speed)
print("Model Milage: ",modelx.milaeage)