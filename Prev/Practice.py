def start_smoking(bars,boxes):
    cigs = 0
    boxes = boxes + bars * 10
    cigs =  cigs + boxes * 18
    butts = cigs
    count = cigs
    while butts >= 5:
        cigs = butts // 5
        butts = cigs + butts % 5
        count += cigs
    return count
print(start_smoking(0,1))