# TO-DO: Complete the selection_sort() function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_index = arr[i]
        j = i
        while j > 0 and curr_index < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr_index


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # Assume this is the highest value
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # for i in range(len(arr)):
    #     j = i
    #     for j in range(len(arr)-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]

    # return arr
    indexing_length = len(arr)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
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
