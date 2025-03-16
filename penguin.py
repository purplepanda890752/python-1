class Bird:
    def __init__(self):
        print("Bird is ready to fly")
    def whosiThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whisiThis(self):
        print("Penguin")
    def run(self):
        print("run faster")

peg = Penguin()
peg.whosiThis()
peg.swim()
peg.run()