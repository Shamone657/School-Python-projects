#Iterative#
def Factorial (n):
    
    total = 1
    
    for i in range(1,n+1):
        
        total *= i
        
    print(total)
    
number = 5

Factorial(number)

#Example#
def myFun(x):
    
    if x < 1:
        
        return
    
    myFun(x-1)
    
    print(x)
    
myFun(5)

#Recursive#
def fact(n):
    
    if n == 1:
        
        return 1
    
    else:
        
        ans = n * fact(n - 1)
        
    return ans
        
print(fact(6))