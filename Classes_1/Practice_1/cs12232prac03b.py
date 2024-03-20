from Classes_1.Practice_1.oj import MinReadyArray

class Metropolis:
    H = MinReadyArray
    def __init__(self, H: list[int]):
        self.m = H
    def expand_left(self, h: int) -> None:
        self.m.insert(0, h)
    def __len__(self):
        return len(self.m)
    def cost(self, i: int, j: int) -> int | None:
        if 0 <= i <= j < len(self.m):
            count = 0
            for z in range(i, j+1):
                if self.m[z] != min(self.m[i:j+1]):
                    count += abs(self.m[z] - min(self.m[i:j+1]))
            return count * 7
        else:
            return None
m = Metropolis([3, 1, 4, 1, 5])