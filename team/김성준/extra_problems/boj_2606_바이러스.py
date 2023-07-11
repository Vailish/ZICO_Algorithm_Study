# boj_2606_바이러스
# https://www.acmicpc.net/problem/2606

# dfs
def dfs(v):
    global cnt
    cnt += 1
    visited[v] = True

    for next_v in graph[v]:
        if visited[next_v] == 0:
            dfs(next_v)


# 정점의 수
v = int(input())
# 간선의 수
n = int(input())
# 방문 리스트
visited = [0 for _ in range(v+1)]

# 그래프 채우기
graph = [[] for _ in range(v+1)]  # 0은 버림
for _ in range(n):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

cnt = 0

dfs(1)
print(cnt-1)  # 출발점은 제외해야 하기 때문
