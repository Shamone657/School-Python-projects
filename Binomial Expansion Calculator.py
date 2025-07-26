import math

while True:
 
 print("------------------------------------------------------------------------------------------------------------------------------------------------------") #seperator 

 print("a and b are coefficients, x are variables and c is the power")

 Q = input("What type of equation do you have? (1) (a + bX)^c, (2) (aX + b)^c, (3) (a + b)^c, (4) (aX +bX)^c \n")

 if Q == "1": #copied code

  print("(a+bX)^c")
  
  A=int(input('a = '))
 
  B=int(input('b = '))
 
  C=int(input('c = '))
 
  x=2
 
  expansion=str(A**C)+' + '+str(B*C)+'x'
  
  while x<(C+1):
    
    nCr = (math.factorial(C))/((math.factorial(x))*(math.factorial(C-x)))
    
    expansion = expansion+' + '+str((B**x)*int(nCr))+'x^'+str(x)
    
    x=x+1
  
  print(expansion)

 if Q == "2":
  
  print("Placholder")

 if Q == "3":
  
  print("Placholder")

 if Q == "4":
  
  print("Placholder")

 else:

  continue