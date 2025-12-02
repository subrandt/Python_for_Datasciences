"""
Educational goal:
Understand generators and the yield keyword by creating a progress bar.

What is yield?
yield pauses a function and returns a value,
then resumes from where it stopped.
This creates a generator: an object that produces values one at a time.

Why use yield here?
We need to produce values one by one AND display progress between each value.

Example:
    for i in ft_tqdm(range(5)):
        # Do something
    # Displays: 100%|[=====>]| 5/5
"""


import sys


def ft_tqdm(lst: range) -> None:  # Should be -> Generator
    """
    Decorator that displays a progress bar for iterations.

    Note: The return type should technically be Generator[Any, None, None]
    since this function uses yield, but the subject specifies -> None.

    Args:
        lst: A range object to iterate over

    Yields:
        Each element of the range, one at a time
    """
    total = len(lst)

    for i, item in enumerate(lst):
        # Calculate progress
        current = i + 1
        percent = (current / total) * 100

        # Create progress bar (simple version)
        bar_length = 50
        filled = int(bar_length * current / total)
        bar = '=' * filled + '>' + ' ' * (bar_length - filled - 1)

        # Display progress bar
        # \r returns cursor to start of line (overwrites previous output)
        sys.stdout.write(f'\r{percent:3.0f}%|[{bar}]| {current}/{total}')
        sys.stdout.flush()  # Force immediate display

        # Yield the current item (generator magic happens here)
        # Function pauses here, returns item, then resumes on next iteration
        yield item

    # Print newline at the end
    print()
