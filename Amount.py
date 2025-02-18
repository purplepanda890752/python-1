

def calculate_due_amount():
    """Calculates the remaining amount a customer owes after making a payment."""
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        amount_paid = float(input("Enter the amount paid: $"))

        if amount_paid > total_bill:
            change = amount_paid - total_bill
            print(f"Payment complete! Change to return: ${change:.2f}")
        elif amount_paid == total_bill:
            print("Payment complete! No amount due.")
        else:
            due_amount = total_bill - amount_paid
            print(f"Amount still due: ${due_amount:.2f}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the function
calculate_due_amount()
