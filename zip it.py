zip1 = {2,3,5,6}
zip2 = {'a', 'b', 'c', 'd',}
keepinpocket = list(zip(zip1,zip2))
print(keepinpocket, "\n")

list1 = [10,20,30,40,50]
list2 = [100,200,300,400,500,600]

for x, y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ['dominos', 'KFC', 'burger king', 'papa johns', 'subway']
prices = [3000,2000,5000,4000,2500]

new_dict = {stocks: prices for stocks, prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))