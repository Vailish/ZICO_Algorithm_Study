# DFS와 BFS - silver2
# https://www.acmicpc.net/problem/1260
def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for next_v in sorted(graph[v]):
        if not visited[next_v]:
            dfs(next_v)


def bfs(v):
    queue = [v]
    visited[v] = True
    result = []
    while queue:
        v = queue.pop(0)
        result.append(v)
        for next_v in sorted(graph[v]):
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
    print()
    print(*result)


def solution():
    global graph, visited
    N, M, V = map(int, input().split())
    visited = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    dfs(V)
    visited = [0] * (N + 1)
    bfs(V)


solution()
