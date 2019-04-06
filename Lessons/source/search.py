#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    if array[index] != item:
        return linear_search_recursive(array, item, index + 1)
    else:
        return index

    return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    left = 0
    right = (len(array) - 1)
    mid = (len(array) // 2)

    # If value is not in the range of the sorted array, return None
    if item < array[left] or item > array[right]:
        return None

    #NOTE: This is not the optimal way to about this issue of catching infinite loop errors
    iterations = 0 #if the number of iterations passes half the len of the arary, then return None

    while True:
        if array[mid] == item:
            return mid
        elif array[mid] < item: # We're going Right!
            left = mid
            # right stays the same
            mid = round((mid+right) / 2)

        elif array[mid] > item: # We're going Left!
            right = mid
            mid = round((mid+left) / 2)



    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):

    if left == None and right == None: # initialize variables on the first iteration
        left = 0
        right = (len(array) - 1)
        print('left:', left)
        print('right:', right)
        return binary_search_recursive(array, item, left, right)


    mid = round((left+right)/2) #Averaged index of left and right index values

    # print("mid: ", mid)


    if array[mid] == item: # Found the item between left and right
        return mid
    elif array[mid] < item: # We're going Right!
        left = mid
        return binary_search_recursive(array, item, left, right)
    elif array[mid] > item: #We're going Left!
        right = mid
        return binary_search_recursive(array, item, left, right)



arr = [1,2,3,4,5]
names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
# print(binary_search_iterative(arr, 2))

print(binary_search_recursive(arr, 4))
# print(binary_search_recursive(names, 'Nick'))
