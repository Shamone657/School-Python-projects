def Selection_Sort(arr):

    for i in range(len(arr)):

        min_idx = i

        for j in range(i+1, len(arr)):

            if arr[min_idx] > arr[j]:

                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

my_list = [64, 25, 12, 22, 11, 5, 90, 1, 3, 0]

print("Unsorted array:", my_list)

sorted_list = Selection_Sort(my_list)

print("Sorted array:", sorted_list)