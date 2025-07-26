password = input("Enter your password")

if len(password) > 8 and any(chr.isdigit() for chr in password):
    
    print("Your password is strong")
    
else:
    
    print("Your password is weak")