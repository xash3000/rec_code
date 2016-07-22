"""
recursively binary search array
"""


def rec_bs(arr, element):
    """
    recursively binary search
    """
    if len(arr) == 1:
        return arr[0] == element
    else:
        first, last = 0, len(arr)
        mid = (first + last) // 2
        if arr[mid] == element:
            return True
        elif arr[mid] > element:
            return rec_bs(arr[:mid], element)
        elif arr[mid] < element:
            return rec_bs(arr[mid:], element)


# test
arr, element = list(range(100)), 99
print(rec_bs(arr, element))
