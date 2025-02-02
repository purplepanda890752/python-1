# WAP to do Sum of Whole Numbers
n = int(input("Please enter the number of terms you want the sum of"))
sum = 0

#for loop
for i in range(2, n+1):
    sum = sum + i
    print("\n SUM=", sum)