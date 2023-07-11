# 2563. 색종이

n = int(input())
# 100x100 2차원 배열 선언
arr = [[0] * 100 for _ in range(100)]
count = 0
# 색종이가 붙은 부분을 1로 바꿔준다
for _ in range(n):
    col, row = map(int, input().split())
    for i in range(100 - row - 10, 100 - row):
        for j in range(col, col + 10):
            if arr[i][j] != 1:
                arr[i][j] = 1
                # 색종이가 붙은 부분을 모두 더하면 넓이!
                count += 1
print(count)
