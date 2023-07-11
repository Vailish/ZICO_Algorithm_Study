def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    for num in sorted(list(reserve)):
        if num - 1 in lost:
            lost.remove(num - 1)
        elif num + 1 in lost:
            lost.remove(num + 1)
    return n - len(lost)
