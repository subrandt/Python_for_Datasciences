"""
Educational goal:
Understand how Python's built-in filter() works.

What is filter()?
Filter takes a list and a function, and keeps only items where
the function returns True.

Example:
    numbers = [1, 2, 3, 4, 5]
    # Keep only numbers > 3
    result = filter(lambda x: x > 3, numbers)
    # result = [4, 5]
"""


def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    # CASE 1: function is None
    # If no function is given, keep only "truthy" values
    # Truthy = values that are considered True in Python
    # Examples of truthy: 1, "hello", [1,2], True
    # Examples of falsy: 0, "", [], False, None
    if function is None:
        # Example: ft_filter(None, [0, 1, False, "hello"])
        # Will keep: [1, "hello"] (only truthy values)
        return [item for item in iterable if item]

    # CASE 2: function is provided
    # Apply the function to each item
    # Keep the item only if function(item) returns True
    # Example: ft_filter(lambda x: x > 3, [1, 2, 3, 4, 5])
    # Will test: 1>3? No. 2>3? No. 3>3? No. 4>3? Yes! 5>3? Yes!
    # Result: [4, 5]
    return [item for item in iterable if function(item)]
