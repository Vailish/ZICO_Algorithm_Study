def pinball(r, c):
    global max_v
    for d in range(4):
        sr, sc = r, c
        cnt = 0
        while True:
            nr, nc = sr + dr[d], sc + dc[d]
            if not 0 <= nr < n or not 0 <= nc < n:
                # d = blocks[5][d]
                # sr, sc = nr, nc
                # cnt += 1
                # continue
                sr, sc = r, c
                cnt *= 2
                cnt += 1

            elif matrix[nr][nc] in {0, -1}:
                sr, sc = nr, nc

            elif 6 <= matrix[nr][nc] <= 10:
                for pos in blocks[matrix[nr][nc]]:
                    if (nr, nc) != pos:
                        sr, sc = pos
                        break
            else:
                d = blocks[matrix[nr][nc]][d]
                cnt += 1
                sr, sc = nr, nc

            if matrix[sr][sc] == -1 or (sr == r and sc == c):
                if cnt > max_v:
                    max_v = cnt
                break


# 상하좌우 0 1 2 3
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

t = int(input())
for tc in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    blocks = [[0], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2], [], [], [], [], []]
    max_v = 0
    # 웜홀쌍 찾기
    for i in range(n):
        for j in range(n):
            if 6 <= matrix[i][j] <= 10:
                blocks[matrix[i][j]].append((i, j))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                pinball(i, j)

    print(f"#{tc + 1} {max_v}")