def sum_array(arr: list[int]) -> None:
    if arr == [] or arr is None:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)