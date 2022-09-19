def chk(board_1):
    start = board_1[0]  # (15, 8)
    result = 0
    for i in range(1, d):
        if board_1[i][1] > start[1]:
            result += abs(board_1[i][0] - start[0]) * (max_location - start[1])
            if board_1[i][1] == max_location:
                break
            start = board_1[i]
    return result


d = int(input())
board = []
max_location = 0
for _ in range(d):
    l, h = map(int, input().split())
    if max_location < h:
        max_location = h
    board.append((l, h))
board.sort(key=lambda x: (x[0], x[1]))
answer = (board[-1][0] - board[0][0] + 1) * max_location
answer -= chk(board) + chk(board[::-1])
print(answer)
