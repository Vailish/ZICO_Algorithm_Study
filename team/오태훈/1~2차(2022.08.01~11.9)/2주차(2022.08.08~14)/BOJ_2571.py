# 2571. 색종이-3

n = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(n):
    col, row = map(int, input().split())
    for i in range(100 - row - 10, 100 - row):
        for j in range(col, col + 10):
            if arr[i][j] != 1:
                arr[i][j] = 1

max_s = 0
s = 0
for row in range(100):
    for col in range(100):
        