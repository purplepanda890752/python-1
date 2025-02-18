def check_age():
    """Validates user age input and checks if it's even or odd."""
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Error: Age cannot be negative!")
        elif age > 150:  # Assuming 150 is the maximum reasonable age
            print("Error: Age entered is too high to be valid!")
        else:
            if age % 2 == 0:
                print(f"The entered age {age} is valid and EVEN.")
            else:
                print(f"The entered age {age} is valid and ODD.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer for age.")

# Run the function
check_age()
