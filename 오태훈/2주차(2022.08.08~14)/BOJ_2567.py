# 2567. 색종이-2

n = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(n):
    col, row = map(int, input().split())
    for i in range(100 - row - 10, 100 - row):
        for j in range(col, col + 10):
            if arr[i][j] != 1:
                arr[i][j] = 1

row_way = [-1, 1, 0, 0]  # 상 하 좌 우
col_way = [0, 0, -1, 1]
count = 0
for row in range(100):
    for col in range(100):
        if arr[row][col] == 1:
            for i in range(4):
                r = row + row_way[i]
                c = col + col_way[i]
                if 0 <= r < 100 and 0 <= c < 100:
                    if arr[r][c] == 0:
                        count += 1
                if r < 0 or r >= 100 or c < 0 or c >= 100:
                    count += 1
print(count)
