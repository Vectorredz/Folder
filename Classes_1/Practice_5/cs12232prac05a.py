import collections
from pytest import raises
from typing import Sequence
from oj import Point as Pt

def is_axis_aligned(polygon: Sequence[Point]) -> bool:
    if not len(polygon) == 4 and not all(count == 1 for count in collections.Counter(polygon).values()):
        raise ValueError
    elif len(polygon) == 4 and all(count == 1 for count in collections.Counter(polygon).values()):
        return True
    else:
        return False