import collections

vertices = [1,2,3,4,5,6,6]
print(all(count == 1 for count in collections.Counter(vertices).values()))