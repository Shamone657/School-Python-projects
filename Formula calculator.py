import math

while True:
 
 print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #seperator 

 formula = input("Select a formula: Area of circle (ac,1) / Length of circle (lc,2) / Area of cylinder (acy,3) / Volume of cyilinder (vc,4) / Area of sphere (as,5) / Volume of sphere (vs,6)\n") #formula selector

 formula = formula.lower()

 if formula in ["1" , "AC" , "ac" , "Ac"]: #formula for area of circle

  radius = float(input("Enter radius"))

  area = math.pi * radius ** 2

  print(area)

 elif formula in ["2" , "lc" , "LC" , "Lc"]: #formula for length of circle
   
  radius = float(input("Enter radius"))

  area = 2 * math.pi * radius

  print(area)

 elif formula in ["3" , "ACY" , "acy" , "Acy" , "ACy"]: #formula for area of cylinder
 
  radius = float(input("Enter radius"))

  height = float(input("Enter height"))

  area = 2 * math.pi * radius * height

  print(area)

 elif formula in ["4" , "vc" , "VC" , "Vc"]: #formula for volume of cylinder
 
  radius = float(input("Enter radius"))

  height = float(input("Enter height"))
 
  volume = math.pi * radius ** 2 * height

  print(volume)

 elif formula in ["5" , "as" , "AS" , "As"]: #formula for area of sphere
 
  radius = float(input("Enter radius"))

  area = 4 * math.pi * radius ** 2 

  print(area)

 elif formula in ["6" , "vs" , "VS" , "Vs"]: #formula for volume of sphere

  radius = float(input("Enter radius"))
 
  volume = (4/3) * math.pi * radius ** 3 

  print(volume) 

 else: 
  
  print("Try again")
  
  continue
 
 

