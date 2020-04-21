# component 3 - compares input to randomly generated
# gives feedback e.g. "you won" or "you lose"

# imports random
import random

# integer checking function
def int_check(question, low, high):
    valid = False
    error = "Please enter 1, 2 or 3"
    while not valid:
        try:
            response = int(input("Enter 1 for rock, 2 for paper or 3 scissors "))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()


# main code
rps_random = ["rock", "paper", "scissors"]

rock = 1
paper = 2
scissors = 3
rps_input = int_check("Enter 1 for rock, 2 for paper or 3 scissors ", 1, 3)
if rps_input == rock:
    print("You chose rock")
elif rps_input == paper:
    print("You chose paper")
else:
    print("You chose scissors")
print()

chosen = random.choice(rps_random)
print(chosen)

if rps_input == 1 and chosen == paper:
    print("You lose")
elif rps_input == 1 and chosen == scissors:
    print("You win!")
elif rps_input == 2 and chosen == rock:
    print("You win!")
elif rps_input == 2 and chosen == scissors:
    print("You lose")
elif rps_input == 3 and chosen == rock:
    print("You lose")
elif rps_input == 3 and chosen == paper:
    print("You win!")
