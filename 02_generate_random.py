# component 2 - generate random
# create list (rock, paper, scissors)
# generate random 15 times for testing purposes

import random

rps_random = ["rock", "paper", "scissors"]

for item in range(1, 15):
    chosen = random.choice(rps_random)
    print(chosen, end="\t")
