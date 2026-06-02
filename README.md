# string-utils

A small collection of handy Python string utility functions.

## Functions

- `reverse_string(s)` — reverses a string
- `is_palindrome(s)` — checks if a string is a palindrome (case-insensitive, ignores spaces)
- `word_count(s)` — counts the number of words in a string

## Usage

```python
from string_utils import reverse_string, is_palindrome, word_count

reverse_string("hello")      # "olleh"
is_palindrome("racecar")     # True
is_palindrome("A man a plan a canal Panama")  # True
word_count("hello world")    # 2
```

## Running tests

```
python -m pytest tests/
```
