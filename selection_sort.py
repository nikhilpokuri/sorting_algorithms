def selectionSort(arr):
    """
    push the minimum elements to left by swapping the curr element with right most minimum element
    """
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
arr = [1, 2, 5, 3, 4]
selectionSort(arr)
print(arr)