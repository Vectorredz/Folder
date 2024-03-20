from typing import Sequence, Collection, Mapping, TypeVar, MutableSequence

T = TypeVar("T")

def f(seq: Sequence[T]) -> Sequence[T]:
    return seq[::-1]

print(f([50,50,100]))

def g(xss: list[list[T]]) -> list[T]:
    return [x for xs in xss for x in xs]

print(g([[1, 2], [3, 4]]))

def h(m: dict[T, T]) -> Collection[T]:
    ret: dict[T, T] = {}
 
    for k, v in m.items():
        ret.setdefault(v, []).append(k)
 
    return ret

print(h({'alex': 1}))