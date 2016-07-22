"""
recursively reverse array
"""


def rec_rev(arr):
    """
    rec_rev([1]) => [1]
    rec_rev([1, 2]) => [2, 1]
    rec_rev([1, 2, 3, 4, 5]) = > [5, rec_rev([2, 3, 4]) ,1]
    """
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        return [arr[-1], arr[0]]
    else:
        return [arr[-1]] + rec_rev(arr[1:-1]) + [arr[0]]


# test
arr = range(100)
print(rec_rev(arr))
