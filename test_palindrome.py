from main import is_palindrome

def test_palindrome_happy():
    assert is_palindrome("racecar") is True

def test_palindrome_unhappy():
    assert is_palindrome("video") is False

def test_palindrome_empty():
    assert is_palindrome("") is True