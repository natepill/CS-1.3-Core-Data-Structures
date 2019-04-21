#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    # Time Complexity: O(n*m)
    # Space Complexity: O(1)


    ''' Old code that works is commented out'''
    # There should be a way to save the index of where we are (index wise) when we are comparing text to pattern
    # for index, letter in enumerate(text):
    #     try:
    #         if letter == pattern[0]:
    #         # Compare the slice of text from the current index to the len of pattern
    #             if pattern == text[index: (index + len(pattern))]:
    #                 return True # pattern == slice
    #             # If comparion is not the same, then continue the iteration
    #     except:
    #         return True
    # # Pattern was not found during the entire iteration
    # return False



    # Check to see if there are any starting patterns in the text
    return len(find_all_indexes(text, pattern)) > 0




def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)


    # Time Complexity: O(n*m)
    # Space Complexity: O(1)



    ''' Old code that works is commented out'''
    # O(nm) solution, n = len of text, m len of pattern

    # for index, letter in enumerate(text):
    #     try:
    #         if letter == pattern[0]:
    #         # Compare the slice of text from the current index to the len of pattern
    #             if pattern == text[index: (index + len(pattern))]:
    #                 return index # pattern == slice
    #             # If comparion is not the same, then continue the iteration
    #     except:
    #         return 0
    # # Pattern was not found during the entire iteration
    # return None



    # Return the first found index of all indexes that start a pattern
    try:
        return find_all_indexes(text, pattern)[0]
    except:
        return None



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Time Complexity: O(n*m)
    # Space Complexity: O(1)



    # list of indexes that indicate the start of pattern
    pattern_starting_indexes = list()

    if pattern == '':
        for index in range(0, len(text)):
            pattern_starting_indexes.append(index)
        return pattern_starting_indexes

    for index, letter in enumerate(text):
        if letter == pattern[0]:
            # Compare the slice of text from the current index to the len of pattern
            if pattern == text[index: (index + len(pattern))]:
                pattern_starting_indexes.append(index) # pattern == slice
            # If comparion is not the same, then continue the iteration

    # Pattern was not found during the entire iteration
    return pattern_starting_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()

    # print(contains('banana', 'na'))
    print(find_index('abc',''))
    print(find_all_indexes('abc',''))

    # print(len(''))
