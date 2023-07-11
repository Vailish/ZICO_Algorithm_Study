n, k = map(int, input().split())
board = [0] * 12
for _ in range(n):
    i, j = map(int, input().split())
    board[i * 6 + j - 1] += 1
answer = 0
for num in board:
    if num > 0:
        answer += num // k
        if num % k > 0:
            answer += 1
print(answer)
