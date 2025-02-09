def perimeter_triangle(a, b, c):
    return a + b + c

def perimeter_square(side):
    return 4 * side

def perimeter_rectangle(length,width):
    return 2 * (length + width)

def circumfrence_circle(radius):
    return 2 * 3.14 * radius

print("\nPerimeter Calculator")
print("a. Triangle")
print("b. Square")
print("c.Rectangle")
print("d. Circumfrence (circle)")
print("e. Exit")

choice = input ("choose an option (a-e)")

if choice == 'a':
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))

elif choice == 'b':
            side =  float(input("Enter the side length: "))
            print(f"Perimeter of square: {perimeter_square(side)}")
            
elif choice =='c':
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            print(f"Perimeter of Rectangle: {perimeter_rectangle(length, width)}")

elif choice == 'd':
            radius = float(input("Enter the radius: "))
            print(f"Circumfrence of a Circle: {circumfrence_circle(radius)}")

elif choice == 'e':
            print("Exiting the Calculator. GOODBYEE!!")

else:
            print("Invalid choice! Please select a valid option")

