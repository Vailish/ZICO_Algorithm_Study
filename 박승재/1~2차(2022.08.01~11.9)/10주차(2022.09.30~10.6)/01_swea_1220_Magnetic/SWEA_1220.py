import sys

sys.stdin = open("input.txt")


def sol():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        chk = False
        for j in range(n):
            if not chk and board[j][i] == 1:
                chk = True
            elif chk and board[j][i] == 2:
                answer += 1
                chk = False
    print(answer)


for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')
    sol()
