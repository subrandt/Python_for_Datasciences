"""Count module"""


def count_in_list(lst: list, item: any) -> int:
    """
    Count occurrences of an item in a list.

    Args:
        lst: The list to search in
        item: The item to count

    Returns:
        int: Number of occurrences
    """
    return lst.count(item)
