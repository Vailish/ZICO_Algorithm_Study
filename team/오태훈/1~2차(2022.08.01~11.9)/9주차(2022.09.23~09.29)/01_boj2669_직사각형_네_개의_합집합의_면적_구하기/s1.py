# 2669. 직사각형 네개의 합집합의 면적 구하기

cnt_arr = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(y1, y2):
        for col in range(x1, x2):
            cnt_arr[row][col] = 1
result = 0
for arr in cnt_arr:
    result += sum(arr)
print(result)
