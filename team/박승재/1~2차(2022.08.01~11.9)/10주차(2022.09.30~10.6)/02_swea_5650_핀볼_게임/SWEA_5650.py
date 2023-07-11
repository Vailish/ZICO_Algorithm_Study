def sol():
    def chk(x, y, direction):
        cnt = 0
        nx, ny = x, y
        while True:
            nx, ny = nx + dx[direction], ny + dy[direction]
            if nx in (-1, n) or ny in (-1, n) or board[nx][ny] == 5:
                return cnt * 2 + 1

            if (nx, ny) == (i, j) or board[nx][ny] == -1:
                return cnt

            if 1 <= board[nx][ny] < 5:
                cnt += 1
                direction = block[board[nx][ny] - 1][direction]
            elif 6 <= board[nx][ny] <= 10:
                nx, ny = worm_hole[board[nx][ny] - 6][worm_hole[board[nx][ny] - 6].index((nx, ny)) - 1]

    # 상하좌우
    # 0 1 2 3
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    block = [(1, 3, 0, 2), (3, 0, 1, 2), (2, 0, 3, 1), (1, 2, 3, 0)]
    for tc in range(1, int(input()) + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        worm_hole = [[] for _ in range(5)]
        for i in range(n):
            for j in range(n):
                if 6 <= board[i][j] <= 10:
                    worm_hole[board[i][j] - 6].append((i, j))
        answer = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    for d in range(4):
                        result = chk(i, j, d)
                        if answer < result:
                            answer = result
        print('#{} {}'.format(tc, answer))


sol()
