# noinspection PyShadowingBuiltins,PyUnusedLocal


def compute(x, y):
    """
    Return the sum of two integers.

    param x: a positive integer between 0-100
    param y: a positive integer between 0-100
    @return: an Integer representing the sum of the two numbers
    """
    if not (isinstance(x, int) and isinstance(y, int)):
        return 'Please enter only integers, example: 40'
    if not ((x >= 0 and x <= 100) and (y >= 0 and y <= 100)):
        return 'Please enter only integers between 0 and 100.'
    return x + y
