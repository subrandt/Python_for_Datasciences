"""
Educational goal:
Learn to create a complete autonomous program with argument handling,
user input, and text analysis.

This program counts different types of characters in a text:
upper/lower case letters, punctuation, spaces, and digits.
"""

import sys
import string


def analyze_text(text: str) -> None:
    """
    Analyze a text and print statistics about its characters.

    Args:
        text: The string to analyze

    Returns:
        None: Prints the analysis directly to stdout
    """
    # Count total characters
    total = len(text)

    # Count uppercase letters
    upper_count = sum(1 for c in text if c.isupper())

    # Count lowercase letters
    lower_count = sum(1 for c in text if c.islower())

    # Count punctuation marks
    # string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    punctuation_count = sum(1 for c in text if c in string.punctuation)

    # Count spaces (includes spaces, tabs, newlines)
    space_count = sum(1 for c in text if c.isspace())

    # Count digits
    digit_count = sum(1 for c in text if c.isdigit())

    # Print results
    print(f"The text contains {total} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Main function: handle arguments and call text analysis.
    """
    # Check number of arguments (argv[0] is script name)
    if len(sys.argv) == 1:
        # No argument: prompt user for input
        print("What is the text to count?")
        text = input()
    elif len(sys.argv) == 2:
        # Exactly one argument: use it
        text = sys.argv[1]
    else:
        # More than one argument: print error and exit
        print("AssertionError: more than one argument is provided")
        return

    # Analyze the text
    analyze_text(text)


if __name__ == "__main__":
    main()
