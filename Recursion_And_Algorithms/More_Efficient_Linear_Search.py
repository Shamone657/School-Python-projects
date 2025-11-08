myList = [2,5,4,1,7,9]

n = 4

def linear_search(arr,key):
    
    for i in range(len(arr)):
        
        if arr[i] == key:
            
            return i
        
    return - 1

print(linear_search(myList,n))