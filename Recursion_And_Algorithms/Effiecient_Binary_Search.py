myList = [1,3,6,9,12,17,25,29,34,38,45,49,51,52]

target = 17

def binarySearch(list, target):

    low = 0
    
    high = len(list) - 1

    while low <= high:

        mid = (low + high) // 2
        
        guess = list[mid]

        if guess == target:
            
            return mid
        
        if guess > target:
            
            high = mid - 1
        
        else:
            
            low = mid + 1

    return None

print(binarySearch(myList,target))