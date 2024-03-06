def shopping_outcomes(n: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(len(n)):
        for j in range(i, len(n)):
            meow: list[int] | int = n[i:j+1]
            result.append(meow)
            result.sort(key = lambda x: (len(x),x), reverse = True)
    return result 
print(shopping_outcomes([10, 1, 10, 1]))

'''For two distinct outcomes A and B (represented as lists of enjoyments), we say that A has a higher quality than B if at least one of the following is
true:
A is strictly longer than B. (The more shops, the better.)
A and B have equal length, and if i is the lowest index such that A[i] and B[i] are unequal, then A[i] is greater than B[i]. (The earlier
shops give a more lasting impression.)
'''