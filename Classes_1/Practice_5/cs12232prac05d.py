from typing import Generic, Mapping, TypeVar
K = TypeVar("K")
V = TypeVar("V")
class BiDict(Generic[K, V]):
    def __init__(self, b: Mapping[K, V]):
        self.b: Mapping[K, V] = b
    def __getitem__(self, k: K):
        try:
            return self.b[k]
        except:
            raise KeyError
    
    def __setitem__(self, k: K, v: V):
        pass
    def __len__(self):
        return len(self.b)
    def __pop__(self, k: K):
        pass
    def keys_with_value(self, v: V):
        pass
