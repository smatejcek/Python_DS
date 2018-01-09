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
    Doctest:
        >>> mode
    """
    counter = {i:0 for i in nums}
    for i in range(len(nums)):
        counter[nums[i]] += 1
    return sorted(counter, key = lambda key: counter[key])[-1]
