def dfs(x, y, direction, dis):
    global answer
    if dis >= answer and visit_dir[x][y][direction] <= dis:
        return

    visit_dir[x][y][direction] = dis
    if 0 < board[x][y] <= 2:
        nx, ny = x + dx[direction], y + dy[direction]
        if (nx, ny) == (0, -1):
            answer = min(answer, dis)
            return
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny, direction, dis + 1)
            visit[nx][ny] = False
    elif board[x][y] > 2:
        i = 0
        if direction == 0 or direction == 1:
            i = 2
        for d in range(i, i + 2):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) == (0, -1):
                answer = min(answer, dis)
                return
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                dfs(nx, ny, d, dis + 1)
                visit[nx][ny] = False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = n ** 2
    inf = n ** 2
    visit_dir = [[[inf] * 4 for _ in range(n)] for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    dfs(n - 1, n - 1, 2, 1)
    # print(*visit_dir, sep="\n")
    print(f'#{tc} {answer}')
