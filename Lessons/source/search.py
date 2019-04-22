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

    # Check to make sure there isn't an index error
    if index >= (len(array)):
        return None

    # If the value of the array at index is NOT the item, then recall the function with an incremented by 1 index
    if array[index] != item:
        return linear_search_recursive(array, item, index + 1)
    else: #We found the value at index!
        return index

    # The value wasn't found :(
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

    # initialize some variables
    left = 0
    right = len(array)-1
    mid = right // 2

    print("First left:", left)
    print("First right:", right)
    print("First mid:", mid)


    # Iterations will continue until the left bound surpasses the right bound
    while left <= right:

        if array[mid] == item: # Item found!
            return mid

        elif array[mid] < item: # Go right!
            print('mid value {} is less than item: {}'.format(array[mid], item))
            left = mid + 1

        else: # Go left!
            right = mid - 1
            print('mid value {} is greater than item: {}'.format(array[mid], item))


        mid = left + (right - left) // 2 # Half the index!

    return None # Item not found!





def binary_search_recursive(array, item, left=None, right=None):

    if left == None and right == None: # initialize variables on the first iteration
        left = 0
        right = (len(array) - 1)
        # print('left:', left)
        # print('right:', right)
        return binary_search_recursive(array, item, left, right)

    mid = round((left+right)/2) #Averaged index of left and right index values

    if array[mid] == item: # Found the item between left and right
        return mid

    elif mid == left or mid == right: # Catches infinite loop error
        return None

    elif array[mid] < item: # We're going Right!
        left = mid
        return binary_search_recursive(array, item, left, right)

    elif array[mid] > item: #We're going Left!
        right = mid

        return binary_search_recursive(array, item, left, right)


if __name__ == '__main__':
    # arr = [1,2,3,4,5]
    names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']


    # print(linear_search(names, 'Winnie'))
    # print(linear_search(names, 'Kojin'))
    # print(linear_search(names, 'Brian'))
    # print(linear_search(names, 'Nabil'))
    # print(linear_search(names, 'Julia'))
    # print(linear_search(names, 'Alex'))
    # print(linear_search(names, 'Nick'))
    #
    # print(linear_search(names, 'Jeremy') is None)
    # print(linear_search(names, 'nobody') is None)


    # print(binary_search(names, 'Alex'))
    # print(binary_search(names, 'Brian'))
    # print(binary_search(names, 'Julia'))
    # print(binary_search(names, 'Kojin'))
    # print(binary_search(names, 'Nabil'))
    # print(binary_search(names, 'Nick'))
    # print(binary_search(names, 'Winnie'))
    # print(binary_search(names, 'Jeremy'))
    # print(binary_search(names, 'nobody'))


# names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
