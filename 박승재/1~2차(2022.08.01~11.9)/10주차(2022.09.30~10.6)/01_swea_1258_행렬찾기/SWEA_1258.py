def sol():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = []
    chk = set()
    for i in range(n):
        for j in range(n):
            if (i, j) in chk:
                continue
            if board[i][j] > 0:
                chk_col = 1
                chk_row = 1
                for i1 in range(i + 1, n):
                    if board[i1][j] == 0:
                        break
                    chk_col += 1
                for j1 in range(j + 1, n):
                    if board[i][j1] == 0:
                        break
                    chk_row += 1
                for i2 in range(i, i + chk_col):
                    for j2 in range(j, j + chk_row):
                        chk.add((i2, j2))
                answer.append([chk_col, chk_row])
    answer.sort(key=lambda x: (x[0] * x[1], x[0]))
    print(len(answer), end=' ')
    for i in range(len(answer)):
        print(*answer[i], end=' ')
    print()


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    sol()
