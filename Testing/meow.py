def f(xs: list[str]) -> str:
    return xs[0]

x = []
x.append(1)

y = f([1, 2, 3])

zs = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
]

for z in zs:
    match z:
        case []:
            print('Empty')
        case [a]:
            print('One element')
        case [a, b]:
            print('Two elements')
        case _:
            print('More than two elements')