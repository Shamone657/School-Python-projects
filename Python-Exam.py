# Q1

num = float(input("Enter a number: \n")) #Asks user for number

if num > 0: #if number is greater than 0
    
    print("The number is positive")
    
elif num < 0: #if number is less than 0
    
    print("The number is negative")
    
else: #if number is 0
    
    print("The number is 0")



# Q2

x = 0

while x != 100: #if x is not equal to 100
    
    y = x + x #adds even numbers to total
    
    x += 2 #adds even numbers 
    
print(y) #prints sum of total




# Q3

x = 0

for x in range (1,51): # prints 1-50
    
    if x % 5: 
        
        print(x)
        
    else:
        
        print("Buzz")
        
x = 0

for x in range (1,51): #prints 1-50
    
    if x % 3:
        
        print(x)
        
    else:
        
        print("Fizz")
        


# Q4

l = []

for y in range(1,8):
    
    x = int(input("Enter a number: \n")) #asks for a number
    
    l.append(y) #adds number to list
    
print("Original list is", l) #prints list
