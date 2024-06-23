arr = [3, 2, 1, 5, 10, 4]
def insertionSort(arr):
    """
    move the current element to the correct position in left sorted sub-array
    """
    for i in range(1, len(arr)):
        key = arr[i] #key that needs to be positioned in correct place
        j = i - 1
        while key < arr[j] and j >= 0:
            arr[j+1] =arr[j]
            j -= 1
        arr[j+1] = key
insertionSort(arr)
print(arr)