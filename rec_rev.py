"""
recursively reverse array
"""


def rec_rev(arr):
    """
    rec_rev([1]) => [1]
    rec_rev([1, 2, 3, 4, 5]) = > [rec_rev([2, 3, 4, 5]), 1]
    """
    if len(arr) == 1:
        return arr
    else:
        return rec_rev(arr[1:]) + [arr[0]]


# test
arr = list(range(100))
print(rec_rev(arr))
