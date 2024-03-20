from typing import Sequence, TypeVar

T = TypeVar("T")
def swap_pairs(l: Sequence[T]) -> list[T] | None:
    l = list(l)
    new_l: list[T] = []
    if len(l) % 2 != 0:
       raise ValueError('Nigger')
    for pairs in range(0, len(l), 2):
        l[pairs], l[pairs + 1] = l[pairs + 1], l[pairs]
        a = l[pairs], l[pairs + 1]
        new_l.extend(a)

    return new_l

assert swap_pairs((3, 1, 4, 1, 5, 9)) == [1, 3, 1, 4, 9, 5]
assert swap_pairs(('Kelly', 'Alec', 'Xochitl', 'Valentin')) == ['Alec', 'Kelly', 'Valentin', 'Xochitl']

# test ValueError when odd
try:
    swap_pairs([1, 2, 3])
except ValueError:
    pass
else:
    assert False, "should have raised ValueError!"