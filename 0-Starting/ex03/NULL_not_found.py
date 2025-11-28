"""
Educational goal:
Understand the different "falsy" values in Python and their types.
Not all "false" values are the same!

This module identifies 5 types of NULL values:
None, NaN, 0, empty string, False.
"""

import math


def NULL_not_found(object: any) -> int:
    """
    Identifies and prints different types of NULL/falsy values in Python.

    Args:
        object: Any Python object to check

    Returns:
        int: 0 if a NULL type is found, 1 otherwise
    """
    # Check for None (NoneType)
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0

    # Check for NaN (float)
    # NaN is special: NaN != NaN, so we use math.isnan()
    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
        return 0

    # Check for False (bool) - MUST be before int check!
    # False is technically an int in Python, so test bool first
    if isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0

    # Check for 0 (int)
    if isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0

    # Check for empty string (str)
    if isinstance(object, str) and object == '':
        print(f"Empty: {type(object)}")
        return 0

    # Type not found
    print("Type not Found")
    return 1
