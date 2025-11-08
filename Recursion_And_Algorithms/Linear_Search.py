myList = [4,23,21,1,22,67,34,84,63,69]

def binarySearch(list,  target):

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