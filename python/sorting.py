from random import randint
from re import L

def get_unsorted_list(len=100):
    numbers = []
    for i in range(len):
        numbers.append(randint(1, 100))
    print(numbers)
    return numbers


def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    return numbers

def confirm_sorting_algo(input_list, algorithm):
    algo_sorted = input_list.copy()
    algo_sorted = algorithm(algo_sorted)
    input_list.sort()
    print(input_list)
    if sorted == algo_sorted:
        return True
    else:
        return False

if __name__ == "__main__":
    print(confirm_sorting_algo(get_unsorted_list(), sort_list))
        