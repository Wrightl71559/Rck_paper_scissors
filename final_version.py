# component 9 - point system
# add in a point system so the game ends when user reaches -2 points or 5 points

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

# Intro
print("Welcome to the rock paper scissors game")
print("The rules are the same as normal rock paper scissors")
print("except this game has a point system")
print("to win you need 5 points (you get 1 point by winning a round)")
print("but if you reach -2 points (you lose half a point if you lose a round) you lose the game!")
print("Good luck!!")
print()

rps_random = ["rock", "paper", "scissors"]

rounds = 1
points = 0
rounds_won = 0
rounds_lost = 0
rounds_drawn = 0

keep_going = ""
while keep_going == "" and 5 > points > -2:

    print("-- Round {} --".format(rounds))
    print()

    rock = 1
    paper = 2
    scissors = 3

    # get user input
    rps_input = int_check("Enter 1 for rock, 2 for paper or 3 scissors ", 1, 3)
    print()
    if rps_input == rock:
        print("You chose rock")
    elif rps_input == paper:
        print("You chose paper")
    else:
        print("You chose scissors")
    print()

    chosen = random.choice(rps_random)
    print("We chose {}".format(chosen))

    # compare user input to randomly generated
    if rps_input == 1 and chosen == "paper":
        rps_statement("## You lose ##", "#")
        rounds_lost += 1
        points -= 0.5
    elif rps_input == 1 and chosen == "scissors":
        rps_statement("** You win! **", "*")
        rounds_won += 1
        points += 1
    elif rps_input == 2 and chosen == "rock":
        rps_statement("** You win! **", "*")
        rounds_won += 1
        points += 1
    elif rps_input == 2 and chosen == "scissors":
        rps_statement("## You lose ##", "#")
        rounds_lost += 1
        points -= 0.5
    elif rps_input == 3 and chosen == "rock":
        rps_statement("## You lose ##", "#")
        rounds_lost += 1
        points -= 0.5
    elif rps_input == 3 and chosen == "paper":
        rps_statement("** You win! **", "*")
        rounds_won += 1
        points += 1
    else:
        rps_statement("== It's a tie ==", "=")
        rounds_drawn += 1

    print()
    print("points: {}".format(points))
    print()

    rounds += 1

    # end game if player has won or lost
    if points >= 5:
        rps_statement("!! Congratulations! You've won the game !!", "!")
    elif points <= -2:
        rps_statement("// Sorry, you've lost the game //", "/")
    else:
        keep_going = input("To start the next round press <enter> ")
        print()

print()
print("Thank you for playing :)")
print()

# game summary statistics
print(" *** Game Statistics *** ")
print(" Rounds won: {}".format(rounds_won))
print(" Rounds lost: {}".format(rounds_lost))
print(" Rounds drawn: {}".format(rounds_drawn))
