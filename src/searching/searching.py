
def linear_search(arr, target):
    index = 0  # index starts at beginning
    for i in arr:  # traverse thru array
        if i == target:  # if i is == target
            return index  # return the index
        index += 1  # otherwise index + 1
    return -1  # do this if not found


# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    if len(arr) == 0:  # if the array is empty
        return -1
    low = 0  # first element
    high = len(arr) - 1  # last element

    while low <= high:
        middle = (low+high)//2  # make a mid point
        if arr[middle] == target:  # if midpoint is target
            return middle  # return the midpoint
        elif target < arr[middle]:  # get rid of unneeded side
            # change endpoint to middle (get rid of unneccessary)
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1  # get rid of other side
    return -1  # not found
