def get_jumps(cycle_list: list[int], k: int):
    # given 5 elements in an array
    # while or for loops make a list slice
    jumps: int = 0
    start: int = cycle_list[0]
    index = 0
    cycles = 1
    for _ in range(cycles):
        print(cycle_list[index])
        index = (index + 1) % len(cycle_list)
    
        


print(get_jumps([1, 5, 7, 8, 9], 2))