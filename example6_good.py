from inspect import getdoc


def complex_function(x, y, z):
    """
    Calculates the sum of three numbers.

    Args:
        x (int): first number
        y (int): second number
        z (int): third number

    Returns:
        int: the sum of x, y, and z
    """
    return x + y + z

# Вариант 1
print(complex_function.__doc__)

# Вариант 2
help(complex_function)
# Вариант 3
getdoc(complex_function)
