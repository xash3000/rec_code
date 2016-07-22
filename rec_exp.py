"""
recursive exponentiation
"""


def rec_exp(x, n):
    """
    recursive exponentiation

    x^0 = 1
    x^n = x * x^(n-1)
    """
    if n == 0:
        return 1
    else:
        return x * rec_exp(x, n - 1)


# test
print(rec_exp(3, 4))    # 81
