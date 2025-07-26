g = int(input("Enter your grade in %: \n"))

if g >= 90 and g <= 100:
    
    print("Grade A")
    
elif g >= 80 and g<= 89:
    
    print("Grade B")
    
elif g >= 70 and g<= 79:
    
    print("Grade C")
    
elif g >= 60 and g<= 69:
    
    print("Grade D")
    
elif g<= 60 and g>= 0:
    
    print("FAIL")
    
else:
    
    print("ERROR")