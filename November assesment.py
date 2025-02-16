
#Question 1

L = []

newL = []

for i in range (5):
    
    num = int(input("Enter a number:\n"))
    
    L.append(num + 1)
    
print(L)

print("Programme end")

#Question 2

bed = int(input("How hard do you want your bed?\n"))

pillow = int(input("How hard do you want your pillow?\n"))

colour = input("What colour do you want your bed?\n")

colour = colour.lower()

if bed == 100 and pillow == 100 and colour == "red":
    
    print("This bed is for you")
    
else:
    
    print("This bed is not for you")
    
print("Programme end")


#Question 3

num = 13

guess = 0

while guess != num:
    
    guess = int(input("Guess a number:\n"))
    
    if guess < num:
        
        print("Enter a higher number")
        
    elif guess > num:
        
        print("Enter a lower number")
        
    elif guess == num:
        
        print("Congragulations, you win!\n")
        
    else:
        
        print("Invalid guess")

print("Programme end")