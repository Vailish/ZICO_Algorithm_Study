# 쉬운 최단거리 - silver1
# https://www.acmicpc.net/problem/14940


# 넓이 우선탐색(bfs)를 수행하여 최단 거리를 구한다!
# input을 받을때 갈수 있는 길은 미리 -1로 변경하고
# bfs를 돌리면서 이동시 덮어 씌우는 방법으로 진행
from collections import deque


def solution():
    def bfs():
        dq = deque()
        dq.append((r, c, 0))
        visited[r][c] = 1

        while dq:
            x, y, d = dq.popleft()
            field[x][y] = d
            # 우, 하, 좌, 상
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == -1 and not visited[nx][ny]:
                    dq.append((nx, ny, d+1))
                    visited[nx][ny] = 1

    n, m = map(int, input().split())
    visited = [[0] * m for _ in range(m)]
    field = []
    for i in range(n):
        chk = list(map(int, input().split()))
        cnt = 0
        tmp = []
        for val in chk:
            if val == 1:
                tmp.append(-1)
            elif val == 2:
                r, c = i, cnt
                tmp.append(val)
            else:
                tmp.append(val)
            cnt += 1

        field.append(tmp)

    bfs()
    for lst in field:
        print(*lst)


solution()
