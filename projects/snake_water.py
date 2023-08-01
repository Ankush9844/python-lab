
# COMPUTER =   S   W   G
#              1   2   3
# PLAYER = S   D   W   L 

#          W   L   D   W 

#          G   W   L   D
import random #random is a module which can be geanrate a random no. between the defined range.

computer = random.randint(1, 3)

user = int(input("Please select one of the option(1 2 3): "))

print("Computer input",computer)
print("User input",user)

if computer == user :
    print("Tie")
 
if computer == 1 and (user == 2 or user == 3):
    print("user win")
if computer == 2 and user == 1 :
    print("user lose")

if computer == 2 and user == 3 :
    print("user win")

if computer == 3 and (user == 1 or user == 2) :
    print("user lose")
