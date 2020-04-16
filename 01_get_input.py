# component 1 - get input
# ask user to  enter rock, paper or scissors
# check that input is valid


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
