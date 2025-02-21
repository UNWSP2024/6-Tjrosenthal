
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

#Tanner Rosenthal
#2/21/2025
#Average Dice Sum

import random
def ranDice():
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    roll_sum = n1 + n2
    return roll_sum

total = 0
for roll in range(100):
    roll_sum = ranDice()
    total += roll_sum

avg = total/100
rounded_avg = round(avg, 2)
print(rounded_avg)
