from Classes_1.Practice_1.oj import MinReadyArray

class MollyMarketplace:
    def __init__(self, n: int, t: int):
        self.n = n
        self.t = t
        self.m = MinReadyArray()

    def rent(self, payment: int, income: int) -> bool:
        if payment >= self.t and len(self.m) != self.n:
            self.m.append_right(income)
            return True
        return False

    def lowest_income(self, i: int, j: int) -> int:
        if j < len(self.m):
            ok = self.m.min(i, j)
            assert ok
            return ok

        ok = self.m.min(i, len(self.m))
        assert ok
        return ok

class DesmondMarketplace:
    def __init__(self, s: int, t: int):
        self.s = s
        self.t = t
        self.m = MinReadyArray()

    def rent(self, payment: int, income: int) -> bool:
        if payment >= self.t and len(self.m) != self.s:
            self.m.append_left(income)
            return True
        return False

    def lowest_income(self, i: int, j: int) -> int:
        try1 = self.s - len(self.m)
        new_i = i - try1
        new_j = j - try1
        if new_i < 0:
            new_i = 0
        ok = self.m.min(new_i, new_j)
        assert ok
        return ok



