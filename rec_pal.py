"""
recursively check if string is palindrome
"""


def rec_pal(string):
    """
    string is palindrome if it's read the same both backward and forward

    rec_pal("a") => True
    rec_pal("ab") => "a" == "b"
    rec_pal("abcdefg") => "a" == "g" and rec_pal("bcdef")
    in general:
        True if:
            string[0] == string[-1] and rec_pal(string[1:-1])
    """
    if len(string) <= 1:
        return True
    elif len(string) == 2:
        return string[0] == string[-1]
    else:
        # remove whitespaces
        string = string.strip()
        return string[0] == string[-1] and rec_pal(string[1:-1])


# test
string = "radar"
print(rec_pal(string))  # True
