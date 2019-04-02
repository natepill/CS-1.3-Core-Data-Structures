#!python
import string

'''
A base is the max value (non-inclusive) of what the digit can go up to.

I am going to zip a digits 0-9 and lowercase letters with numbers up to 36 to create a dictionary that will map
'''
nums_and_letters = '{}{}'.format(string.digits, string.ascii_lowercase) # [0-9a-z]
up_to_36 = (list(range(0, 36))) #list of ints up to 36
digit_mapper = dict(zip(nums_and_letters, up_to_36)) # maps digit to its decimal value up to 36
'''
Base 12:
Example: 36 base12 ===> 42 in base 10
(12^0) + 6
(12^1) * 3

Example 107 base12 ===> 151 in base 10
(12^0) + 7
(12^1) * 0 (I would have to make sure it adds nothing if given 0)
(12^ 2) * 1
'''


# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# NOTE: Accomodate both uppercase both lowercase when decoding/encoding. So I have to determine to use either depending on the input


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    base_10_value = 0
    # Unsure if I need to enumerate, enumeration would give me the right power to raise the digits to
    for exponent, digit in enumerate(digits[::-1]):
        if exponent == 0:
            base_10_value += digit_mapper[digit] # On the first index, we are just adding that pure value
        elif int(digit) == 0: # We want to continue the iteration if 0 is present, because its just a placeholder value
            continue
        else:
            base_10_value += (base ** exponent) * digit

    return base_10_value



    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()

    print(decode('2', 3))
