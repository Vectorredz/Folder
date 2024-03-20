from collections import Counter
from typing import Sequence

def generate_histogram(data: Sequence[int]):
    for i in data:
        if i < 0:
            raise ValueError
    counts = [0]*10
    for num in data:
        counts[int(str(abs(num))[0])] += 1

    cmax = max(counts)

    histogram = []
    for i in range(20, -1, -1):
        row = []
        for j in range(10):
            if i <= 20 * counts[j] // cmax:
                row.append("##")
            else:
                row.append("..")
        histogram.append(".".join(row))
    return histogram

print(generate_histogram((31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95,  2, 88, 41, 97,
            16, 93, 99, 37, 51,  5, 82,  9, 74, 94, 45, 92, 30, 78, 16, 40, 62, 86, 20, 89,
            98, 62, 80, 34, 82, 53, 42, 11, 70, 67, 98, 21, 48,  8, 65, 13, 28, 23,  6, 64,
            70, 93, 84, 46,  9, 55,  5, 82, 23, 17, 53, 59, 40, 81, 28, 48, 11, 17, 45,  2)))