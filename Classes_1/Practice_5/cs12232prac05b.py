from collections import Counter
from pytest import raises
from typing import Sequence

def first_digits(data: Sequence[int]) -> Counter[int]:
    for i in data:
        if not i < 0:
            counter = Counter(int(str(number)[0]) for number in data if 1 <= int(str(number)[0]) <= 9)
            return counter
        else:
            raise ValueError

def test_first_digits_invalid():
    with raises(ValueError):
        first_digits((1, 1, -1, 1, 1))

def test_first_digits_valid():
    assert first_digits((0, 12, 34, 0)) == Counter[int]((0, 1, 3, 0))

    # data from Pike County
    counts: Counter[int] = first_digits((
            31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95,  2, 88, 41, 97,
            16, 93, 99, 37, 51,  5, 82,  9, 74, 94, 45, 92, 30, 78, 16, 40, 62, 86, 20, 89,
            98, 62, 80, 34, 82, 53, 42, 11, 70, 67, 98, 21, 48,  8, 65, 13, 28, 23,  6, 64,
            70, 93, 84, 46,  9, 55,  5, 82, 23, 17, 53, 59, 40, 81, 28, 48, 11, 17, 45,  2,
        ))

    # check keys
    assert set(counts.keys()) <= set(range(10))

    # check values
    for key, expected_value in [
            (0, 0),
            (1, 7),
            (2, 11),
            (3, 5),
            (4, 10),
            (5, 10),
            (6, 8),
            (7, 4),
            (8, 12),
            (9, 13),
        ]:
        assert counts[key] == expected_value