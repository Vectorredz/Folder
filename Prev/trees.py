from itertools import product
print(sum(1 for x in product(range(3),repeat=5) if all(y in x for y in range(3)) and any(x.count(y)!=2 for y in range(3))))