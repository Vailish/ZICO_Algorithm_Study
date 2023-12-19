# 숨바꼭질 - silver1
# https://www.acmicpc.net/problem/1697
from collections import deque


def solution():
    N, K = map(int, input().split())
    if N == K:
        print(0)
        return
    queue = deque()
    queue.append((N, 0))
    visited = [False] * 200000

    while queue:
        p, d = queue.popleft()
        visited[p] = True
        if p == K:
            print(d)
            return

        # 앞뒤로 1칸 이동할 경우
        # 2배로 이동할 경우
        for next_v in [p*2, (p+1), (p-1)]:
            if 0 <= next_v <= 100000 and not visited[next_v]:
                queue.append((next_v, d + 1))


solution()
