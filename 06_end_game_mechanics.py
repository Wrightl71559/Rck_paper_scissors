# component 6 - end game mechanics
# loop game

# imports random
import random


# statement generator function
def rps_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print


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

rounds_won = 0
rounds_lost = 0
rounds_drawn = 0

keep_going = ""
while keep_going == "":
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
    print("We chose {}".format(chosen))
    print()

    if rps_input == 1 and chosen == "paper":
        rps_statement("## You lose ##", "#")
        rounds_lost += 1
    elif rps_input == 1 and chosen == "scissors":
        rps_statement("** You win! **", "*")
        rounds_won += 1
    elif rps_input == 2 and chosen == "rock":
        rps_statement("** You win! **", "*")
        rounds_won += 1
    elif rps_input == 2 and chosen == "scissors":
        rps_statement("## You lose ##", "#")
        rounds_lost += 1
    elif rps_input == 3 and chosen == "rock":
        rps_statement("## You lose ##", "#")
        rounds_lost += 1
    elif rps_input == 3 and chosen == "paper":
        rps_statement("** You win! **", "*")
        rounds_won += 1
    else:
        rps_statement("== It's a tie ==", "=")
        rounds_drawn += 1

    print("points: {}".format(rounds_won))
    print()

    keep_going = input("Press <enter> to play again or any key to quit ")
    print()
    print("Thank you for playing :)")
    print()
