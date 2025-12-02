"""
Exercise 07: Dictionaries SoS

Educational goal:
Learn to use dictionaries to store and retrieve data efficiently.

What is Morse code?
A way to encode text using dots (.) and dashes (-).
Each letter/number has its own pattern.

Example:
    S = ...
    O = ---
    SOS = ... --- ...
"""

import sys


# Morse code dictionary
# Each character is a key, its Morse code is the value
# Note: Each code ends with a space for separation
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def encode_to_morse(text: str) -> str:
    """
    Encode a text string into Morse code.

    Args:
        text: String to encode (alphanumeric + spaces only)

    Returns:
        str: Morse code representation

    Raises:
        AssertionError: If text contains invalid characters
    """
    # Convert to uppercase (Morse code uses uppercase)
    text = text.upper()

    # Validate: check if all characters are valid
    # Valid characters: letters (A-Z), digits (0-9), spaces
    for char in text:
        # Check if character is alphanumeric or space
        if not (char.isalnum() or char == " "):
            # Invalid character found (like $, !, etc.)
            raise AssertionError("the arguments are bad")

    # Encode each character to Morse
    morse_code = ""
    for char in text:
        # Get the Morse code for this character from dictionary
        # Example: char = "S" → NESTED_MORSE["S"] = "... "
        morse_code += NESTED_MORSE[char]

    # Remove the trailing space at the end
    return morse_code.strip()


def main():
    """
    Main function: validate arguments and encode to Morse code.
    """
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    text = sys.argv[1]

    # Try to encode the text
    try:
        morse = encode_to_morse(text)
        print(morse)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
