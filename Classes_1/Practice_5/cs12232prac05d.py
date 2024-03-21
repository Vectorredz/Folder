from typing import Generic, TypeVar, Mapping

K = TypeVar('K')
V = TypeVar('V')

class BiDict(Generic[K, V]):
    def __init__(self, initial_contents: Mapping[K, V]):
        self._forward = dict(initial_contents)
        self._backward = {v: k for k, v in initial_contents.items()}

    def __getitem__(self, k: K):
        if self._forward[k]:
            return self._forward[k]
        else:
            raise ValueError

    def __setitem__(self, k: K, v: V):
        if k in self._forward:
            del self._backward[self._forward[k]]
        if v in self._backward:
            del self._forward[self._backward[v]]
        self._forward[k] = v
        self._backward[v] = k

    def __len__(self):
        return len(self._forward)

    def pop(self, k: K):
        if k not in self._forward:
            value = self._forward.pop(k)
            del self._backward[value]
            return value
        else:
            raise ValueError


    def keys_with_value(self, v: V):
        return {key for key, val in self._forward.items() if val == v}
    
    def  __str__(self):
        return f"{self._backward}"

b = BiDict[str, int]({
        'poe': 3,
        'e': 1,
        'near': 4,
        'a': 1,
        'raven': 5,
        'midnights': 9,
        'so': 2,
        'dreary': 6,
        'tired': 5,
        'and': 3,
        'weary': 5,
    })

print(b)