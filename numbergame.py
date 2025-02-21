import random
playing = True
number = str(random.randint(10,20))
while playing:
    guess = input("give me your best guess")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess was wrong")