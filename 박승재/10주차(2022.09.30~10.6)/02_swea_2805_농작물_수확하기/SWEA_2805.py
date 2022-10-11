def sol():
    for test_case in range(1, int(input()) + 1):
        n = int(input())
        board = [list(map(int, list(input()))) for _ in range(n)]
        n //= 2
        answer = sum(board[n])
        for i in range(1, n + 1):
            answer += sum(board[n + i][i:-i])
            answer += sum(board[n - i][i:-i])
        print('#{} {}'.format(test_case, answer))


sol()
