class Food:

    def __init__(self):
        self.__food_price = 900

    def sell(self):
        print("Selling price: {}".format(self.__food_price))

    def setFoodPrice(self, price):
        self.__food_price = price

f = Food()
f.sell()

f.__food_price = 1000 
f.sell()

f.setFoodPrice(1000)
f.sell()
