# 연결 요소의 개수 - silver2
# https://www.acmicpc.net/problem/11724
def solution():
    N, M = map(int, input().split())

    # 몇 덩이인지 찾는 것
    # 그래프를 그린 후, dfs를 돌려 확인
    edge = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        edge[v1].append(v2)
        edge[v2].append(v1)
    visited = [0] * (N+1)

    def dfs(v):
        visited[v] = 1
        for next_v in edge[v]:
            if visited[next_v] == 0:
                dfs(next_v)

    answer = 0
    for n in range(1, N+1):
        if visited[n] == 0:
            dfs(n)
            answer += 1
    print(answer)


solution()
