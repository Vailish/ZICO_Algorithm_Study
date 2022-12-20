# 2578. 빙고

import sys

input = sys.stdin.readline
n = 5
board = [list(map(int, input().split())) for _ in range(n)]
numbers = []
for _ in range(n):
    numbers += list(map(int, input().split()))
bingo_arr = [[] for _ in range((2 * n + 2))]
cnt = 0

for idx, number in enumerate(numbers):
    for row in range(n):
        for col in range(n):
            if board[row][col] == number:
                if row == col:
                    bingo_arr[0].append(number)
                if row + col == 4:
                    bingo_arr[1].append(number)
                bingo_arr[2 + row].append(number)
                bingo_arr[(2 + n) + col].append(number)
                break
    for i in range(2 * n + 2):
        if len(bingo_arr[i]) == 5:
            cnt += 1
            bingo_arr[i].append('end')
    if cnt >= 3:
        print(idx + 1)
        break
