# 효율적인 해킹 - Silver 1
# https://www.acmicpc.net/problem/1325


# 그래프를 그린 뒤,
# DFS를 사용하여 최대 감염 수를 구한 뒤
# 최고 감염 수를 가진 노드를 찾는다

# 시간초과 -> bfs로

import sys
sys.stdin = open('input.txt')

def solution():
    def dfs(v):
        visited[v] = True
        for next_v in graph[v]:
            if not visited[next_v]:
                dfs(next_v)

    N, M = map(int, input().split())  # N = 노드의 수, M = 경로의 수
    edges = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    for v1, v2 in edges:
        graph[v2].append(v1)
    max_count = 0
    max_node = []
    for i in range(1, N+1):
        visited = [0] * (N+1)
        dfs(i)
        tmp = visited.count(True)
        if tmp > max_count:
            max_count = tmp
            max_node = [i]
        elif tmp == max_count:
            max_node.append(i)

    print(*max_node)
    return


solution()

# import sys
# sys.stdin = open('input.txt')
#
#
# def dfs(n):
#     visited[n] = True
#     print(n, end=' ')
#     for next_v in graph[n]:
#         if not visited[next_v]:
#             dfs(next_v)
#
#
# edges = list(map(int, input().split()))
# v = 7 # v = 정점의 수
#
# visited = [False] * (v+1)
# graph = [[] for _ in range(v+1)]
# # graph 채우기
# for i in range(0, len(edges), 2):
#     d1, d2 = edges[i], edges[i+1]
#     graph[d1].append(d2)
#     graph[d2].append(d1)
# dfs(1)
# print()