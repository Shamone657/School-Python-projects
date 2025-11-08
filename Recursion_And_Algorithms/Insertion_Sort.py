'''
def Insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1,n):
        
        for j in range(n):
            
            while arr[i] < arr[j]:
            
                arr[i], arr[j] = arr[j], arr[i]
                
                print(f"{arr}, Each pass{i}")
                
    return(arr)
        
myList = [12,62,73,31,44,22,91,84]

print(myList)

sorted_list = Insertion_sort(myList)

print(f"Your sorted list {sorted_list}")
'''

def Insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1, n):
    
        key = arr[i]
    
        j = i - 1
    
        while j >= 0 and arr[j] > key:
    
            arr[j + 1] = arr[j]
    
            j -= 1
    
        arr[j + 1] = key
    
        print(f"{arr}, After pass {i}")
    
    return arr

myList = [12, 62, 73, 31, 44, 22, 91, 84]

print(myList)

sorted_list = Insertion_sort(myList)

print(f"Your sorted list {sorted_list}")