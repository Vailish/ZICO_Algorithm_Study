# 효율적인 해킹 - Silver 1
# https://www.acmicpc.net/problem/1325


import sys
from collections import deque


sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution():
    def bfs(v):
        queue = deque([v])
        visited = [False] * (N+1)
        cnt = 0
        visited[v] = True
        while queue:
            v = queue.popleft()
            for next_v in graph[v]:
                if not visited[next_v]:
                    cnt += 1
                    queue.append(next_v)
                    visited[next_v] = True

        return cnt


    N, M = map(int, input().split())  # N = 노드의 수, M = 경로의 수
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v2].append(v1)

    max_cnt = 0
    answer = []

    for i in range(1, N+1):
        cnt = bfs(i)
        if max_cnt < cnt:
            max_cnt = cnt
            answer = [i]
        elif max_cnt == cnt:
            answer.append(i)
    print(*answer)

solution()
