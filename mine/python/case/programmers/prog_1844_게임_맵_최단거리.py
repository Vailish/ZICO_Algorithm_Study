# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    dq = deque()
    dq.append((0, 0, 1))
    m = len(maps[0])
    n = len(maps)
    visited = [[0] * m for _ in range(n)]

    while dq:
        r, c, d = dq.popleft()

        # 이동변수 상, 하, 좌, 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        # 델타이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] and not visited[nr][nc]:
                # 목표에 도달했다면, 거리를 반환
                if (nr, nc) == (n - 1, m - 1):
                    return d + 1
                # 아니라면, dq에 추가
                dq.append((nr, nc, d + 1))
                # 여기서 방문처리를 해줘야 다른쪽에서 일로 들어오는 걸 막을 수 있음.
                # 이게 싫다면 maps[nr][nc] = 0 이렇게 처리하고 방문처리를 빼버려라
                visited[nr][nc] = 1

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1],[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
