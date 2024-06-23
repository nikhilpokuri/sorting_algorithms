def mergeSort(arr):
    """
    divide the list into sub-lists until each len(sublist) > 1 and merge by sort
    """
    if len(arr) > 1:
        #divide
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        #merge
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [3, 2, 1, 5, 4, 11, 12]
mergeSort(arr)
print(arr)