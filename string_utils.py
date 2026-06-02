"""Simple string utility functions."""


def reverse_string(s):
    """Reverse a string.

    Args:
        s: The input string to reverse.

    Returns:
        The reversed string.
    """
    return s[::-1]


def is_palindrome(s):
    """Check if a string is a palindrome.

    Args:
        s: The input string.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_count(s):
    """Count the number of words in a string.

    Args:
        s: The input string.

    Returns:
        The number of words.
    """
    if not s.strip():
        return 0
    return len(s.split())
