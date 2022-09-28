board = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(4):
    sr, sc, er, ec = map(int, input().split())
    for i in range(sr, er):
        for j in range(sc, ec):
            if board[i][j] == 0:
                cnt += 1
                board[i][j] = 1
print(cnt)