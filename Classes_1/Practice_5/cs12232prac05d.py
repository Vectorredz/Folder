from typing import Generic, TypeVar, Dict, Set, Mapping

K = TypeVar('K')
V = TypeVar('V')

class BiDict(Generic[K, V]):
    def __init__(self, mapping: Mapping[K, V]):
        self.forward = dict(mapping)
        self.reverse = {}
        for key, value in mapping.items():
            if value not in self.reverse:
                self.reverse[value] = set()
            self.reverse[value].add(key)

    def __getitem__(self, key: K) -> V:
        return self.forward[key]

    def __setitem__(self, key: K, value: V):
        if key in self.forward:
            self.reverse[self.forward[key]].remove(key)
        self.forward[key] = value
        if value not in self.reverse:
            self.reverse[value] = set()
        self.reverse[value].add(key)

    def __len__(self) -> int:
        return len(self.forward)

    def pop(self, key: K) -> V:
        value = self.forward.pop(key)
        self.reverse[value].remove(key)
        if not self.reverse[value]:
            del self.reverse[value]
        return value

    def keys_with_value(self, value: V) -> Set[K]:
        return self.reverse.get(value, set())
