from collections import deque
# bfs로 풀어보자
# 최단거리는 bfs!
def solution(maps):
    len_r = len(maps[0])
    len_c = len(maps)
    def bfs(start, end):
        v1, v2 = start
        queue = deque()
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
    for i in range(len_c):
        for j in range(len_r):
            if maps[i][j] == "S":
                start_point = (i, j)
                break

    # visited 만들기
    visited = [[0 for _ in range(len_r)] for _ in range(len_c)]
    # 시작지점에서 레버까지
    to_lever = bfs(start_point)
    if to_lever == -1:
        return -1
    # 레버에서 종료지점까지
    return

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 답 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # 답 -1