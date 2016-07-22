"""
recursive loop
"""


def rec_loop(start, end, step, function, *args, **kwargs):
    """
    recursive loop

    check if start is less than end then
        call function with start, args and kwargs
        increase start by step
        call rec_loop with start, end, function, *args and **kwargs
    """
    if start < end:
        function(start, args, kwargs)
        start += step
        rec_loop(start, end, step, function, *args, **kwargs)

# test
# print all numbers from 1 to 100


def print_number(number, *args, **kwargs):
    print(number, end=", ")

rec_loop(1, 101, 1, print_number)
