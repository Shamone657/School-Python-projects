w = int(input("Enter your weight in kg"))

h = int(input("Enter your height in cm"))

bmi = w / (h ** 2)

print(bmi)

if bmi <= 18.5:
    
    print("You are underweight")
    
elif 18.5 < bmi <= 24.9:
    
    print("You are normal weight")
    
elif 25 < bmi <= 29.9:
    
    print("You are overweight")
    
elif bmi >= 30:
    
    print("You are obese")