import random

pl = input("Rock, Paper, Scissors, (r/p/s)")

r = 1

p = 2

s = 3

c = ["Rock", "Paper", "Scissors"]

print(random.choice(c))

if pl == 1 and c == "Rock":
    
    print("Its a tie")
    
elif pl == 1 and c == "Paper":
    
    print("Computer won")
    
elif pl == 1 and c == "Scissors":
    
    print("You won")

