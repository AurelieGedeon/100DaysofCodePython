import random

rock_paper_scissors = ["Rock", "Paper", "Scissors"]
user_index = int(input("What do you choose? \n Rock: 0 \n Paper: 1 \n Scissors: 2 \n"))
computer_index = random.randint(0, 2)

if user_index >= 3 or user_index < 0:
    print("You typed an invalid number. You lose! >:(")
else:

    user_choice = rock_paper_scissors[user_index]
    computer_choice = rock_paper_scissors[computer_index]

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = "You win! :)"
    loser = "You lose! :("

    if user_index == computer_index:
        print("It's a tie!")
    elif user_index == 0 and computer_index == 2:
        print(winner)
    elif computer_index == 0 and user_index == 2:
        print(loser)
    elif user_index > computer_index:
        print(winner)
    elif user_index < computer_index:
        print(loser)

