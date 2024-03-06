def flick_switch(lst: list[str]):
    results: list[str] = []
    switch = True
    for i in lst:
        if i == 'flick':
            switch = not switch
        results.append(switch)


print(flick_switch(['codewars', 'flick', 'code', 'wars']))