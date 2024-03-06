class Metropolis:
    def __init__(self):
        H: list[int] = []
        self.m = H
    def expand_left(self, h: int):
        self.m.insert(0, h)
    def len(self):
        return sum(1 for _ in self.m)
    def cost(self) -> int | None:
        if len(self.m) != 0:
            count = 0
            for i in range(len(self.m)):
                while self.m[i] != min(self.m):
                    self.m[i] = abs(self.m[i] - min(self.m))
                    count += 1 
            return count * 7
        else:
            return None
    def display(self) -> list[int] | int | None:
        return self.m

meow = Metropolis()
meow.expand_left(5)
meow.expand_left(1)
meow.expand_left(7)
print(meow.cost())
        

    



