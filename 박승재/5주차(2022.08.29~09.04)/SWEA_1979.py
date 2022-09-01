def sol():
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(chk(board, N, K) + chk(list(zip(*board)), N, K))


def chk(board, n, k):
    result = 0
    for i in range(n):
        total = 0
        for j in range(n):
            if board[i][j] == 1:
                total += 1
                if j == n-1 and total == k:
                    result += 1
            else:
                if total == k:
                    result += 1
                total = 0
    return result


T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    sol()