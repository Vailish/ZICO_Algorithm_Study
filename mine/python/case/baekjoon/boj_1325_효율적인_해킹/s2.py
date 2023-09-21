# 효율적인 해킹 - Silver 1
# https://www.acmicpc.net/problem/1325

# 시간초과 -> bfs로 -> 시간초과... while을 분리해보자

import sys
from collections import deque


sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())  # N = 노드의 수, M = 경로의 수
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v2].append(v1)

    max_num = 0
    max_nodes = []
    result = [0] * (N+1)

    for i in range(1, N+1):
        queue = deque([i])
        visited = [False] * (N+1)
        cnt = 0
        while queue:
            v = queue.popleft()
            visited[v] = True
            for next_v in graph[v]:
                if not visited[next_v]:
                    cnt += 1
                    queue.append(next_v)

        result[i] = cnt

    max_value = max(result)
    for i in range(N+1):
        if result[i] == max_value:
            print(i, end=" ")


solution()
