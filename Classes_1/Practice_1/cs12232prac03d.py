from Classes_1.Practice_1.oj import MinReadyArray
# initially both are empty hence []
# Conditions:
    # no stalls => no rent
    # pay < amount t(UK) pounds => no rent
# which business is earning the least monthly?
class MollyMarketplace:
    def __init__(self, n: int, t: int):
        self.m = MinReadyArray()
        self.n = n
        self.t = t

    def rent(self, payment: int, income: int) -> bool:
        if payment < self.t:
            return False
        if len(self.m) < self.n:
            self.m.append_right(income)
            return True
        return False
    def lowest_income(self, i: int, j: int) -> int:
        if i >= 0 or j <= len(self.m):
            meow = self.m.min(i, j)
            assert meow
            return meow
        meow = self.m.min(i, len(self.m))
        assert meow
        return meow

class DesmondMarketplace:
    def __init__(self, s: int, t: int):
        self.m = MinReadyArray()
        self.s = s
        self.t = t

    def rent(self, payment: int, income: int) -> bool:
        if payment < self.t:
            return False
        if len(self.m) < self.s:
            self.m.append_left(income)
            return True
        return False
    
    def lowest_income(self, i: int, j: int):
        min_income = self.m.min(self.s - i, self.s - j)
        return min_income if min_income is not None else 0

t = 1000000

m = MollyMarketplace(3, t)
d = DesmondMarketplace(5, t)

successful = d.rent(2000000, 10000000)
assert successful

successful = d.rent(20000000, 10000)
assert successful

successful = d.rent(999999, 100000000)
assert not successful

successful = m.rent(2000000, 400000)
assert successful

successful = m.rent(2000000, 300000)
assert successful

successful = m.rent(2000000, 200000)
assert successful

successful = m.rent(2000000, 100000)
assert not successful

assert m.lowest_income(0, 2) == 300000
assert m.lowest_income(1, 3) == 200000
assert d.lowest_income(2, 5) == 10000