mark = float(input("Enter an exam mark between 0 and 100"))

while mark < 0 or mark > 100:
    
    print("Error, mark outside range")
    
    mark = float(input("Re-enter your exam mark"))
    
print("You entered", mark,"well done")