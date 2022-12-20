board = [[0] * 1001 for _ in range(1001)]
num = int(input())
for n in range(1, num+1):
    x1, y1, row, col = map(int, input().split())
    for i in range(y1, y1 + col):
        board[i][x1: x1 + row] = [n] * row
answer = [0] * (num + 1)
for i in range(1001):
    for j in range(1001):
        answer[board[i][j]] += 1
print(*answer[1:], sep="\n")

# board = []
# n = int(input())
# for _ in range(n):
#     x1, y1, row, col = map(int, input().split())
#     box = set()
#     for i in range(x1, x1 + row):
#         for j in range(y1, y1 + col):
#             box.add((i, j))
#     board.append(box)
# sum_board = set()
# for i in range(n - 1, -1, -1):
#     board[i] = board[i] - sum_board
#     sum_board = sum_board | board[i]
#
# for i in range(n):
#     print(len(board[i]))
