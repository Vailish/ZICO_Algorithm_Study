def solution(n, lost, reserve):
    temp = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            temp.append(l)
    lost = temp[:]
    lost_cnt = len(lost)
    lost.sort()
    for l in lost:
        if not reserve:
            break
        if l - 1 in reserve:
            reserve.remove(l - 1)
            lost_cnt -= 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            lost_cnt -= 1

    return n - lost_cnt