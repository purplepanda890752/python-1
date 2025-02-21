import random

while True:
    player = input("Enter a choice (rock, paper, scissors: )")
    game = ["rock", "paper", "scissors"]
    computer = random.choice(game)
    print (f"\n you chose {player}, computer chose {computer} \n")

    if player == computer:
        print(f"Both of you chose {computer}, it's a TIE")
              
    elif player == "rock":
        if computer == "scissors":
            print(f"You win as you have chosen {player}")
        else:
            print(f"You lose as you have chosen {player}")

    elif player == "scissors":
        if computer == "paper":
            print(f"You lose as you have chosen {player}")
        else:
            print(f"You win as you have chosen {player}")

    elif player == "paper":
        if computer == "rock":
            print(f"You win as you hve chosen {player}")
        else:
            print(f"You lose as you have chosen {player}")

    play_again = input(f"You wanna play again (y/n): ")
    if play_again != "y":
        break