def summation(sums):
    return sum(sums)

def printer(array):
    lists = []
    for sums in array:
        print((sums, summation(sums)))
        lists.append(summation(sums))
    return lists

arrays = [[1,2,3],[1,2]]
print(printer(arrays))