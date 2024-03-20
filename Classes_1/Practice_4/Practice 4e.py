from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.s: list[T] = []
    def push(self, value: T) -> None:
        self.s.append(value)
    def pop(self) -> T:
        if self.s:
            return self.s.pop()
        else:
            raise ValueError
    def clear(self) -> None:
        self.s.clear()
    def __len__(self) -> int:
        return len(self.s)
    def __repr__(self):
        return f"{self.s}"

class SnoopingStack(Stack[T]):
    def __init__(self):
        self.m: list[T] = []
        super().__init__()
    def pop(self) -> T:
        val = super().pop()
        self.m.append(val)
        return val
    def history(self):
        return self.m

s = SnoopingStack[int]()

s.push(20)

assert len(s) == 1

res = s.pop()

assert res == 20

s.push(200)

print(s)
