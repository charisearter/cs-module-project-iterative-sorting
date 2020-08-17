# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # go thru array to last item
        cur_index = i  # first element current default smallest
        smallest_index = cur_index  # smallest element
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):  # all elements to right of the position from cur_index
            if arr[cur_index] > arr[j]:  # if element j is < than current element
                smallest_index = j  # new smallest is j
        # swap them
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # for x in range() -> arrange backwards (start at last element, go to 0 index element, in steps of -1 (decrementing steps))
    for x in range(len(arr)-1, 0, -1):
        for y in range(x):  # each element in array to end of x
            if arr[y] > arr[y + 1]:  # if element is greater than next element
                temp = arr[y]  # current element is set to temp
                arr[y] = arr[y+1]  # current element is now next element
                arr[y+1] = temp  # next element is now temp
                # keeps going until end of array
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr


# Monday practice
arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


def multipleOfThree(arr):
    for num in arr:
        if num % 3 == 0:
            print(num)


multipleOfThree(arr)
