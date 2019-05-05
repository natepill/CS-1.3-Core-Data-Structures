import math
import random


def fibonacci(amount_of_numbers=10, number=0, list_of_fibonacci_numbers=list()):
    """Returns a list of fibonacci numbers that has a length equal to amount_of_number variable passed in"""

    # Reached desired length of fibonacci sequence
    if len(list_of_fibonacci_numbers) == amount_of_numbers:
        return list_of_fibonacci_numbers

    # First number of fibonacci sequence
    if number == 0:
        list_of_fibonacci_numbers.append(number) # Add number to list of fibonacci numbers
        return fibonacci(amount_of_numbers, number+1, list_of_fibonacci_numbers) # Next fibonacci number is 0+1

    # Continue recursively finding the next fibonacci number
    else:
        list_of_fibonacci_numbers.append(number)

        # Add the last number of the sequence to the current number to find the next value of the sequence
        last_number = list_of_fibonacci_numbers[-2]
        return fibonacci(amount_of_numbers, number + last_number, list_of_fibonacci_numbers)






# def three_random_groups(arr):
#
#     list_of_groups = list()
#
#     shuffled_arr = random.shuffle(arr)
#
#     list_of_indexes = range(0,len(arr), 3)
#
#     # index = 0
#     index_value = 1
#     next_index = list_of_indexes[index_value]
#     print(arr)
#     print(shuffled_arr)
#     print(list_of_groups)
#     print(list_of_indexes)
#     for index in list_of_indexes:
#         print(index)
#         list_of_groups.append(shuffled_arr[index:next_index])
#         next_index = list_of_indexes[index_value]
#         index_value += 1
#
#
#     return list_of_groups
#

#
# grp1 = []
# while len(arr) is not None:
#
#     while counter < (len(arr)//3):
#         range_of_indexes = range(0, len(arr)-1)
#         random_index = math.random(num_of_students)
#         arr.pop(range_of_indexes[random_index])



if __name__ == "__main__":
    # names = ["Larry", "James", "Harry", "Barry", "Carey", "Nathan", "Lori", "Lauren", "Kae", "Karean", "Joesph"]
    # print(three_random_groups(names))

    fibonacci_sequence = fibonacci(20)
    golden_ratio =  fibonacci_sequence[-1] / fibonacci_sequence[-2] # Calculate Golden Ratio

    print(fibonacci_sequence)
    print(golden_ratio)
