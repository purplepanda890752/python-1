def calculate(amount, tip):
    total = amount*(1+0.01*tip)
    total=round(total,2)
    print(f"your answer is $(total),you need to pay it")

    amount= float(input("enter total amount"))
    tip=  float(input("enter the tip precentage"))
    calculate(amount,tip)

