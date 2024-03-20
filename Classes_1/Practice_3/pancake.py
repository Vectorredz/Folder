from typing import Sequence, List, TypeVar

T = TypeVar("T") 

def stack_like_pancakes(pancake_stacks: Sequence[List[T]]) -> List[T]:
    target_stack: List[T] = []
    for stack in pancake_stacks:
        target_stack.extend(reversed(stack))

    return target_stack

if __name__ == "__main__":
    stacks = [["a", "b"], ["c", "d", "e"], ["f"]]
    result = stack_like_pancakes(stacks)
    print(result)
assert stack_like_pancakes((
        [3, 1],
        [4],
        [1, 5, 9],
    )) == [1, 3, 4, 9, 5, 1]

assert stack_like_pancakes((
        ['strawberry', 'maple'],
        ['waffle', 'chocolate', 'burnt']
    )) == ['maple', 'strawberry', 'burnt', 'chocolate', 'waffle']