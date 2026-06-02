"""Tests for string_utils."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from string_utils import reverse_string, is_palindrome, word_count


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("") == 0
    assert word_count("one") == 1
