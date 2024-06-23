arr = [1, 2, 3, 5, 4]
def bubbleSort(arr):
    """
    check all adjacent elements n times and swap if it is not in ascending order.
    if we didn't perform swap in any iteration, then it's sorted, exit the function
    """
    n = len(arr)
    for i in range(n-1):
        isSwapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                isSwapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if isSwapped == False:
            # if we haven't swapped in this iteration, then come out of the loop
            return
    return arr
bubbleSort(arr)
print(arr)