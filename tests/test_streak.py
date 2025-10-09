import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3, 4]) == 4

def test_mixed_numbers_streak_at_start():
    assert longest_positive_streak([1, 2, -3, 4, 5, 6]) == 3

def test_mixed_numbers_streak_at_end():
    assert longest_positive_streak([-1, 2, 3, -4, 5, 6, 7]) == 3

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, -3, 4, 5, -6, 7, 8, 9]) == 3

def test_single_positive_number():
    assert longest_positive_streak([-1, 2, -3]) == 1

def test_zeros_in_list():
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3