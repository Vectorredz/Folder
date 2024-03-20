from typing import Sequence, List, TypeVar

T = TypeVar("T") 

def swap_pairs(lst: Sequence[T]) -> List[T]:
    if len(lst) % 2 != 0:
        raise ValueError("Input list must have an even number of elements")
    for i in range(0, len(lst), 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst

# Example usage:
if __name__ == "__main__":
    dancers = ["d0", "d1", "d2", "d3", "d4", "d5"]
    result = swap_pairs(dancers)
    print(result)  # Output: ['d1', 'd0', 'd3', 'd2', 'd5', 'd4']
