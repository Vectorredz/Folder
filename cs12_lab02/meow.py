def is_all_possibilities(arr: list[int]):
    n = [x for x in range(min(arr), len(arr))]
    if sorted(n) != sorted(arr):
        return False
    else:
        return True
print(is_all_possibilities([3,2,1,0]))