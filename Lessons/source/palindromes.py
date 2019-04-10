#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


whitespace_or_punctuation = '{}{}'.format(' ',string.punctuation)


# def clean_text(text):
#     '''Shame! Shame! Shame!'''
#     text = text.translate(str.maketrans('', '', string.punctuation))
#     return ''.join(text.split())


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here

    # Also works if text is cleaned
    # text = text.lower()
    # return text == text[::-1]


    left = 0
    right = (len(text) - 1)

    while left != right:
        if text[left].lower() == text[right].lower():
            print('Characters are the same {} = {}'.format(text[left], text[right]))
            left += 1
            right -= 1
            continue

        # Another check to see if the value is punctuation or whitespace, if so move on to next char, but compare to the same char on the other side (need to increment left/right index, but not left/right index)
        elif text[left] in whitespace_or_punctuation:
            print('Came across punctuation from left bound: {}'.format(text[left]))
            left += 1

        elif text[right] in whitespace_or_punctuation:
            print('Came across punctuation from right bound: {}'.format(text[right]))
            right -= 1

        else:
            return False

    return True



    # reversed_text = text[::-1]
    # for index, char in enumerate(text):
    #     if char.lower() != reversed_text[index].lower():
    #         return False
    #     # Another check to see if the value is punctuation or whitespace, if so move on to next char, but compare to the same char on the other side (need to increment left/right index, but not left/right index)
    #     elif char in whitespace_or_punctuation:
    #         pass
    # return True


    # pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):

    # check from index starting left and coming from right
    # stop when left and right == each other, if they do its a palindrome
    # stop when value at left index does not == value at right index


    if left == None and right == None:
        left = 0
        right = (len(text) - 1)

    if left == right:
        return True
    elif text[left].lower() == text[right].lower():
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)
    else:
        return False


    # TODO: implement the is_palindrome function recursively here
    # pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    # print(is_palindrome('  No, On!'))
    # print(is_palindrome('taco cat'))
    # print(is_palindrome('Taco Cat'))
    # print(clean_text('  No, On!'))

    print(is_palindrome('racecar')) # True (Simple test)
    # print(is_palindrome('no, on!')) #True (Complex test)

    # print(whitespace_or_punctuation)
