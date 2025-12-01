"""
Educational goal:
Use filter with lambda to solve a practical problem.

What does this program do?
Takes a text and a number, returns words longer than that number.

Example:
    Input: "Hello the World" and 4
    Process: "Hello" (5 letters > 4) ✓
             "the" (3 letters > 4) ✗
             "World" (5 letters > 4) ✓
    Output: ['Hello', 'World']
"""

import sys
from ft_filter import ft_filter


def main():
    """
    Main function: validate arguments and filter words by length.
    """
    # STEP 1: Check number of arguments
    # sys.argv = ['filterstring.py', arg1, arg2]
    # We want exactly 3 items (script name + 2 arguments)
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    # STEP 2: Get the two arguments
    text = sys.argv[1]
    length_str = sys.argv[2]

    # STEP 3: Validate that second argument is a number
    # Try to convert string to integer
    # Example: "4" → 4 (success)
    # Example: "hello" → ValueError (failure)
    try:
        length = int(length_str)
    except ValueError:
        # If conversion fails, the argument is not a valid number
        print("AssertionError: the arguments are bad")
        return

    # STEP 4: Additional check - first argument must be a string
    # (In practice, sys.argv always gives strings, but good practice)
    if not isinstance(text, str):
        print("AssertionError: the arguments are bad")
        return

    # STEP 5: Split text into individual words
    # split() cuts the string wherever there's a space
    # Example: "Hello the World" → ['Hello', 'the', 'World']
    words = text.split()

    # STEP 6: Filter words by length
    # Lambda function: lambda word: len(word) > length
    # This creates a small function that checks if a word is long enough
    #
    # Example with length = 4:
    #   word = "Hello" → len("Hello") = 5 → 5 > 4 → True → Keep it!
    #   word = "the"   → len("the") = 3   → 3 > 4 → False → Remove it!
    #   word = "World" → len("World") = 5 → 5 > 4 → True → Keep it!
    filtered_words = ft_filter(lambda word: len(word) > length, words)

    # STEP 7: Print the result as a list
    print(filtered_words)


if __name__ == "__main__":
    main()
