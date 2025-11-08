import random

def quick_sort(arr, depth=0):
    print("  " * depth + f"quick_sort({arr})")
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less, depth+1) + [pivot] + quick_sort(greater, depth+1)

# Example usage:
myList = [random.randint(0, 100) for _ in range(10)]
print("Original list:", myList)
sorted_list = quick_sort(myList)
print("Sorted list:", sorted_list)