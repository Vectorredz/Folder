from typing import Sequence, TypeVar

T = TypeVar("T")

def stack_like_pancakes(l: Sequence[list[T]]) -> list[T] | None:
    final_stack: list[T] = []
    for stack in l:
        final_stack.extend(reversed(stack))
    return final_stack
print(stack_like_pancakes([[3, 1],
        [4],
        [1, 5, 9]]))

assert stack_like_pancakes((
        [3, 1],
        [4],
        [1, 5, 9],
    )) == [1, 3, 4, 9, 5, 1]

assert stack_like_pancakes((
        ['strawberry', 'maple'],
        ['waffle', 'chocolate', 'burnt']
    )) == ['maple', 'strawberry', 'burnt', 'chocolate', 'waffle']