#!python

import string


# whitespace_or_punctuation = set('{}{}'.format(' ',string.punctuation))
whitespace_or_punctuation = frozenset((' '+string.punctuation))
print(whitespace_or_punctuation)

# Shame!
# def clean_text(text):
#     text = text.translate(str.maketrans('', '', string.punctuation))
#     return ''.join(text.split())


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):

    left = 0
    right = (len(text) - 1)

    while left < right: # Continue comparing left and right bounds until the indexes are the same

        # Charactacters are the same!
        if text[left].lower() == text[right].lower(): # lowercase the element to remove issues of case sensitivity
            print('Characters are the same {} = {}'.format(text[left], text[right]))
            left += 1
            right -= 1

        # Check to see if the value is punctuation or whitespace, if so move on to next char, comparing to the same char on the other side
        # (need to increment left/right index, but not right/left index)
        elif text[left] in whitespace_or_punctuation:
            print('Came across punctuation from left bound: {}'.format(text[left]))
            left += 1

        # Came across whitespace_or_punctuation from right bound
        elif text[right] in whitespace_or_punctuation:
            print('Came across punctuation from right bound: {}'.format(text[right]))
            right -= 1

        else: #Character comparision was NOT a match, hence not a palindrome
            return False

    # Indexes left and right were the same, hence text is a palindrome
    return True



def is_palindrome_recursive(text, left=None, right=None):

    # First function call sets these values
    if left == None and right == None:
        left = 0
        right = (len(text) - 1)

    # Left index has surpassed the right index, palindrome found! :)
    if left >= right:
        return True

    # Compare characters, if same, then return call to look at the next character from the respective bounds
    elif text[left].lower() == text[right].lower():
        left += 1
        right -= 1
        # return is_palindrome_recursive(text, left, right)

    # Character is in whitespace_or_punctuation from left bound
    elif text[left] in whitespace_or_punctuation:
        left += 1
        # return is_palindrome_recursive(text, left, right)

    # Character is in whitespace_or_punctuation from right bound
    elif text[right] in whitespace_or_punctuation:
        right -= 1

    # Characters are not the same, not a palindrome :(
    else:
        return False

    return is_palindrome_recursive(text, left, right)


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

    # print(is_palindrome('Bb'))
    print(is_palindrome('Bb'))

    # print(is_palindrome('racecar')) # True (Simple test)
    # print(is_palindrome('no, on!')) #True (Complex test)

    # print(whitespace_or_punctuation)
