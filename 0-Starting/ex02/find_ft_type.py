"""
Exercise 02: First function python

Educational goal:
Understand Python's dynamic typing and use type() to identify objects.

This module contains a function that prints the type of various Python objects
in a specific format and always returns 42.
"""


def all_thing_is_obj(object: any) -> int:
    """
    Prints the type of the given object in a specific format.
    
    Args:
        object: Any Python object to analyze
        
    Returns:
        int: Always returns 42
    """
    # Get the type of the object
    obj_type = type(object)
    
    # Check for list, tuple, set, dict
    # Display format: "TypeName : <class 'type'>"
    if obj_type == list:
        print(f"List : {obj_type}")
    elif obj_type == tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type == set:
        print(f"Set : {obj_type}")
    elif obj_type == dict:
        print(f"Dict : {obj_type}")
    
    # Check for string
    # Display format: "string_content is in the kitchen : <class 'str'>"
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    
    # For all other types (int, float, bool, etc.)
    else:
        print("Type not found")
    
    return 42