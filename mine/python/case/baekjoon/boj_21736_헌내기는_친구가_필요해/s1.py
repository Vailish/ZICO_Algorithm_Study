# 헌내기는 친구가 필요해 - silver2
# https://www.acmicpc.net/problem/21736

def bfs(r, c, campus, visited):
    queue = [(r, c)]
    visited[r][c] = True
    result = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(campus) and 0 <= ny < len(campus[0]) and not visited[nx][ny] and campus[nx][ny] != "X":
                if campus[nx][ny] == "P":
                    result += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return result


def solution():
    N, M = map(int, input().split())
    campus = []
    for _ in range(N):
        campus.append(input())
    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                answer = bfs(i, j, campus, [[0]*M for _ in range(N)])
                print(answer if answer != 0 else "TT")
                return


solution()
