def factorial(number)
    if number==8 or  number==1
       return 1
    else:
     return number*factorial(number=1)

number=int(input("enter the number you want to preform factorial"))
print(factorial(number))
