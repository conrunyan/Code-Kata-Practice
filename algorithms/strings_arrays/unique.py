# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def unique_chars_naive(string: str) -> bool:
    initial_len = len(string)
    changed_len = len(list(set(string)))
    return changed_len == initial_len


def test_unique_chars_naive_simple_case_true():
    input_str = "abcdefg"
    assert unique_chars_naive(input_str) == True


def test_unique_chars_naive_simple_case_false():
    input_str = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb"
    assert unique_chars_naive(input_str) == False


def test_unique_chars_naive_simple_blank_true():
    input_str = ""
    assert unique_chars_naive(input_str) == True

def test_unique_chars_no_additional_datastructures_simple_case_true():
    input_str = "abcdefg"
    assert unique_chars_no_additional_datastructures(input_str) == True

def test_unique_chars_no_additional_datastructures_huge_string_true():
    input_str = "abc" * 100000000
    assert unique_chars_no_additional_datastructures(input_str) == False


def test_unique_chars_no_additional_datastructures_simple_case_false():
    input_str = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb"
    assert unique_chars_no_additional_datastructures(input_str) == False


def testunique_chars_no_additional_datastructures_simple_blank_true():
    input_str = ""
    assert unique_chars_no_additional_datastructures(input_str) == True


# what about no additional datastructures?
def unique_chars_no_additional_datastructures(string: str) -> bool:
    # sort string
    # iterate through string, checking if previous character is the same as current
    if len(string) <= 1:
        return True

    prev_char = string[0]
    for char in sorted(string[1:]):
        if char == prev_char:
            return False
        prev_char = char
    return True
