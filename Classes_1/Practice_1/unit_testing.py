from Classes_1.Practice_1.cs12232prac03a import MinReadyArray

# make two instances
arr1 = MinReadyArray()
arr2 = MinReadyArray()

# perform operations
arr1.append_left(40)
arr1.append_right(30)
assert arr1[1] == 30
assert arr1[-1] is None
assert arr2[0] is None
assert arr2.min(-100, 100) is None
arr1.append_left(20)
assert arr1.min(1, 3) == 30
assert arr1.min(0, 3) == 20
arr2.append_left(10)
arr2.append_right(10)
assert arr2.min(-100, 100) == 10
assert arr1.len() == 3
arr1.pop_left()
assert arr1.len() == 2
print(arr1.display())