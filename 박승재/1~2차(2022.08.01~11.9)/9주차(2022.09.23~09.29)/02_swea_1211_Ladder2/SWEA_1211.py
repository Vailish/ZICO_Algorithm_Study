import sys

sys.stdin = open("input.txt")


def sol():
    def dfs(x, y):
        chk.add((x, y))
        for n in range(3):
            nx, ny = x + dx[n], y + dy[n]
            if 0 <= nx < 100 and 0 <= ny < 100 and board[nx][ny] == 1 and (nx, ny) not in chk:
                dfs(nx, ny)
                break
        return

    board = [list(map(int, input().split())) for _ in range(100)]
    answer = (10000, 0)
    for i in range(100):
        if board[0][i] == 1:
            chk = set()
            dfs(0, i)
            if answer[0] > len(chk):
                answer = (len(chk), i)
    print(answer[1])


dx = [0, 0, 1]
dy = [-1, 1, 0]
for _ in range(10):
    print(f'#{int(input())}', end=' ')
    sol()
