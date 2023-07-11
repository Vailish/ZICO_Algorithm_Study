def sol():
    def clean(block_board):
        for d in range(w):
            new = []
            cnt = 0
            for num in block_board[d]:
                if num == 0:
                    cnt += 1
                else:
                    new.append(num)
            block_board[d] = [0] * cnt + new
        return block_board

    def chk(block_board, s):
        visit = set()
        stack = []
        for i in range(h):
            if block_board[s][i] > 0:
                visit.add((s, i))
                stack.append((s, i, block_board[s][i]))
                block_board[s][i] = 0
                break
        while stack:
            x, y, v = stack.pop()
            if v > 1:
                for d in range(4):
                    for t in range(1, v):
                        nx, ny = x + t * dx[d], y + t * dy[d]
                        if nx in (-1, w) or ny in (-1, h):
                            break
                        if block_board[nx][ny] > 0 and (nx, ny) not in visit:
                            visit.add((nx, ny))
                            stack.append((nx, ny, block_board[nx][ny]))
                            block_board[nx][ny] = 0
        return clean(block_board)

    def choice(block_board, t):
        nonlocal answer
        if t == n:
            cnt = 0
            for i in range(w):
                for j in range(h):
                    if block_board[i][j] != 0:
                        cnt += h - j
                        break
            if answer > cnt:
                answer = cnt
            return
        for i in range(w):
            choice(chk([row[:] for row in block_board], i), t + 1)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for tc in range(1, int(input()) + 1):
        n, w, h = map(int, input().split())
        board1 = [list(map(int, input().split())) for _ in range(h)]
        board = []
        for b in zip(*board1):
            board.append(list(b))
        answer = w * h
        choice(board, 0)
        print('#{} {}'.format(tc, answer))


sol()
