def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        small = [] # store all elements that are less than pivot
        large = [] # store all elements that are greater than pivot
        for i in arr:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                large.append(i)
        return quickSort(small) + [pivot] + quickSort(large) #merge (small + middle + large)
arr = [5, 4, 3, 10, 12, 9, 11, 12, 17]
print(quickSort(arr))