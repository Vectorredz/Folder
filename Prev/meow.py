def fury(n):
    result = []
    for i in range(len(n)):
        furies = []
        for j in range(len(n)):
            furies.append(abs(n[i]-n[j]))
        result.append(sorted(furies)[-5])
    return result

print(fury([20, 16, 8, 10, 11, 20, 25]))

