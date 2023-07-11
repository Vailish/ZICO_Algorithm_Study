import sys

sys.stdin = open("input.txt")


def sol():
    def chk_row(x, y):
        number = 0
        while number < length // 2:
            if board[x][y + number] != board[x][y + length - number - 1]:
                return 0
            number += 1
        return 1

    def chk_col(x, y):
        number = 0
        while number < length // 2:
            if board[x + number][y] != board[x + length - number - 1][y]:
                return 0
            number += 1
        return 1

    length = int(input())
    board = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if j < 9 - length:
                cnt += chk_row(i, j)
            if i < 9 - length:
                cnt += chk_col(i, j)
    print(cnt)


for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')
    sol()
