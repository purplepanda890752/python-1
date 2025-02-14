def cube(num)
    return num**3

def func(num):
    if num % 3 ==0:
        return cube(num)
    else:
     return False
     
print cube(cube(9))
print cube(cube(5))