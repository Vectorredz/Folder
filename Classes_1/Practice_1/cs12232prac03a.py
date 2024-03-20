class MinReadyArray:
    def __init__(self):
        self.m: list[int] = []
    def append_right(self, value: int) -> None:
        self.m.append(value)
    def append_left(self, value: int) -> None:
        self.m.insert(0, value)
    def pop_left(self) -> int | None:
        return self.m.pop(0) if self.m else None
    def len(self):
        return sum([1 for _ in self.m])
    def __getitem__(self, i: int) -> int | None:
        return self.m[i] if 0 <= i < len(self.m) else None
    def min(self,i:int,j:int)->int|None:
            if i>j or len(self.m)==0:
                return None
            k=[x for x in range(i,j) if 0<=x<len(self.m)]
            if len(k)==0:
                return None
            array=self.m[k[0]:k[-1]+1]
            min1=self.m[k[0]]
            for i in array:
                if i<min1:
                    min1=i
            return min1
    def display(self) -> list[int] | int | None:
        return self.m

