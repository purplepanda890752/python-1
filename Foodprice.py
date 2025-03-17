class Food:
    def __init__(self):  
        self._price = 10  

    def sell(self):
        print(f"Selling price: ${self._price}")

    def set_price(self, price):
        self._price = price

f = Food()
f.sell()

f.set_price(15)
f.sell()


f._price = 5
f.sell()
