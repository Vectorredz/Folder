class MinReadyArray:
    def __init__(self):
        self.m: list[int] = []
    def append_right(self, value: int) -> None:
        self.m.append(value)
    def append_left(self, value: int) -> None:
        self.m.insert(0, value)
    def pop_left(self) -> int:
        if self.m:
            return self.m.pop(0)
        else:
            raise IndexError
    def pop_right(self) -> int:
        if self.m:
            return self.m.pop()
        else:
            raise IndexError
    def __len__(self) -> int:
        return len(self.m)
    def __getitem__(self, i: int) -> int:
        if not i >=  0 and not i < len(self.m):
            return self.m[i]
        else:
            raise IndexError
    def min(self, i: int, j:int) -> int:
        if i >= j or len(self.m) == 0:
            raise IndexError
        else:
            if i < 0:
                i = 0
            if j > len(self.m):
                j = len(self.m)
            k = [self.m[x] for x in range(i, j)]
            #array of k within i-j
            if len(k) == 0:
                raise IndexError
            array = sorted(k)
            min1 = array[0]

        return min1
    
    def test_MinReadyArray():
        # make two instances
        arr1 = MinReadyArray()
        arr2 = MinReadyArray()

        # perform operations
        arr1.append_left(40)
        arr1.append_right(30)
        assert arr1[1] == 30

        # check IndexErrors
        with pytest.raises(IndexError):
            arr1[-1]
        with pytest.raises(IndexError):
            arr2[0]
        with pytest.raises(IndexError):
            arr2.min(-100, 100)

        arr1.append_left(20)
        assert arr1.min(1, 3) == 30
        assert arr1.min(0, 3) == 20
        arr2.append_left(10)
        arr2.append_right(10)
        assert arr2.min(-100, 100) == 10
        assert len(arr1) == 3
        res: int = arr1.pop_left()
        assert res == 20
        assert len(arr1) == 2