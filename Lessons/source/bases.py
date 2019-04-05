#!python
import string
import math

nums_and_letters = '{}{}'.format(string.digits, string.ascii_lowercase) # [0-9a-z]
up_to_36 = (list(range(0, 36))) #list of ints up to 36
digit_mapper = dict(zip(nums_and_letters, up_to_36)) # maps digit to its decimal value up to 36
inv_digit_mapper = {v: k for k, v in digit_mapper.items()}


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


def decode(digits, base):

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)


    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    base_10_value = 0
    # Unsure if I need to enumerate, enumeration would give me the right power to raise the digits to
    for exponent, digit in enumerate(digits[::-1]):
        if exponent == 0:
            base_10_value += digit_mapper[digit] # On the first index, we are just adding that pure value
        elif digit.isalpha():
            base_10_value += (int(base) ** exponent) * int(digit_mapper[digit])
        elif int(digit) == 0: # We want to continue the iteration if 0 is present, because its just a placeholder value
            continue
        else:
            base_10_value += (int(base) ** exponent) * int(digit)

    return base_10_value





# TODO: Go through and replace all "number" variables to their value using dictionary
# TODO: Need to check logic of if statements, don't think they're right
# TODO: Maybe how I subtract from number is wrong?
def encode(number, base):

    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    highest_power = math.floor(math.log(number, base))
    number_string = ''

    print("Highest Power:", highest_power)

    # Enumerate over powers in reversed
    for exponent in reversed(range(0, highest_power+1)):

    	if number >= base ** exponent:
    		divisor = math.floor(number / (base ** exponent))
            # print('divisor:', divisor)
    		number = number - (divisor * (base ** exponent))
    		number_string += inv_digit_mapper[divisor] # Convert value of divisor to its mapped value in baseX

    	else:
    		number_string += '0'


    return number_string



    '''Working solution for JUST binary'''
    # for exponent in reversed(range(0, highest_power+1)):
    #
    #     if number == 0:
    #         for num in range(0, len(range(0, exponent))+1):
    #             print(num)
    #             number_string += '0'
    #         break
    #     elif (base ** exponent) < (number - (base ** exponent)):
    #         print((base ** exponent) < (number - (base ** exponent)))
    #         number_string += '0'
    #         continue
    #     elif (base ** exponent) == (number - (base ** exponent)):
    #         number_string += '1'
    #         for _ in range(0, len(range(0, exponent))):
    #             number_string += '0'
    #         break
    #
    #     elif (base ** exponent) > (number - (base ** exponent)):
    #         print(number)
    #         number = number - (base ** exponent)
    #         number_string += '1' # will have to change the added string to accomodate the range of the base values, maybe use ascii mapper
    #
    # return number_string








def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)


    return encode(decode(digits, base1), base2)


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
    main()
    # print(decode('10', 2)) # 2
    # print(decode('9', 10)) # 9
    # print(decode('10', 10)) # 10

    # print(decode('a', 16))
    # print(digit_mapper)
    # print(inv_digit_mapper)

    # print(encode(16, 16))
    # print(encode(10, 16))
    # print(encode(45, 2))
