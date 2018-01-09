"""
  Run:
    python -m doctest -v stats.py
"""

def add(numbers):
    return sum(*numbers)

def cubic(lengths, width, height):
    return length * width * height

def means(numbers):
    return sum(numbers) / len(numbers)

def median(nums):
    """ Computes the median of a list of numbers.

    argument: list of numbers
    return: the median

    >>> median([2, 1, 6])
    2
    >>> median([3, 5, 4, 9])
    4.5

    """
    if len(nums) % 2 == 0:
        return sum(sorted(nums)[len(nums) // 2 - 1:len(nums) // 2 + 1]) / 2
    else:
        return sorted(nums)[len(nums) // 2]

def mode(nums):
    """
    Returns the most frequent value in the number_list

    argument: list of number_list
    return: the mode
    """
    counter = {i:0 for i in nums}
    for i in range(len(nums)):
        counter[nums[i]] += 1
    return sorted(counter, key = lambda key: counter[key])[-1]


def variance(numbers, ddof):
    """
    Doctests:
        >>> variance([3, 3, 10, 8, 12, 5, 6], 0)
        10.204081632653061
        >>> variance([3, 3, 10, 8, 12, 5, 6], 1)
        11.904761904761905
    """
#    mean = sum(numbers) / len(numbers)
#    sum_sqrs = sum([(n - mean) ** 2 for n in numbers])
#    return sum_sqrs / (len(numbers) - ddof)
    return sum([(n - sum(numbers) / len(numbers)) ** 2 for n in numbers]) / (len(numbers) - ddof)

def standard_deviation(numbers, ddof):
    """
    Doctests:
        >>> standard_deviation([3, 3, 10, 8, 12, 5, 6], 0)
        3.1943828249996997
        >>> standard_deviation([3, 3, 10, 8, 12, 5, 6], 1)
        3.450327796711771
    """
    return variance(numbers, ddof) ** 0.5
