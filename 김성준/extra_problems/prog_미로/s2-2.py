from collections import deque
# bfs로 풀어보자
# 최단거리는 bfs!
def solution(maps):
    len_r = len(maps)
    len_c = len(maps[0])
    def bfs(start, end):
        v1, v2 = start
        queue = deque([])
        queue.append((v1, v2, 1))

        while queue:
            r, c, d = queue.popleft()

            # 델타 검색 / 상 하 좌 우
            # dr = [-1, 1, 0, 0]
            # dc = [0, 0, -1, 1]
            for dr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr[0]
                nc = c + dr[1]
                if 0 <= nr < len_r and 0 <= nc < len_c and maps[nr][nc] != "X" and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, d + 1))

                    if (nr, nc) == end:
                        return d
        return -1

    # 주요 변수 구하기
    for i in range(len_r):
        for j in range(len_c):
            if maps[i][j] == "S":
                start_point = (i, j)
            elif maps[i][j] == "E":
                end_point = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)

    # visited 만들기
    visited = [[0 for _ in range(len_c)] for _ in range(len_r)]
    # 시작지점에서 레버까지
    to_lever = bfs(start_point, lever)
    if to_lever == -1:
        return -1

    # visited 초기화
    visited = [[0 for _ in range(len_c)] for _ in range(len_r)]
    # 레버에서 종료지점까지
    to_exit = bfs(lever, end_point)
    if to_exit == -1:
        return -1
    return to_lever + to_exit