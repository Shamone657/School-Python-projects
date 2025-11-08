import random

def bubble_sort(myList):

    n = len(myList)

    for j in range(n):

        for i in range(0, n - j - 1):

            if myList[i] > myList[i + 1]:

                temp = myList[i]

                myList[i] = myList[i + 1]

                myList[i + 1] = temp

        print(f"After pass {j + 1}: {myList}")  # Shows the list after each pass

    return myList

"""
Sorts a list using the bubble sort algorithm.
Args:
    myList (list): The list to be sorted.
    Returns:
        list: The sorted list.
"""

myList = [random.randint(1, 100) for _ in range(9)]

print("Unsorted list:", myList)

sortedList = bubble_sort(myList)

print("Sorted list:", sortedList)