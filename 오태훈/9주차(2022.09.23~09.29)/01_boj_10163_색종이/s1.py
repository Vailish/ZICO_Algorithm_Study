# 10163. 색종이
n = int(input())
# 색종이를 놓을 1001x1001평면을 만든다.
arr = [[0] * 1001 for _ in range(1001)]
# 0번 ~ n번까지의 넓이를 저장할 리스트를 만든다. (0번은 사용하지 않는다.)
cnt_arr = [0] * (n)
for num in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    # y부터 높이만큼 row
    for row in range(y, y + h):
        for col in range(x, x + w):
            if arr[row][col] != 0:
                cnt_arr[arr[row][col] - 1] -= 1
                arr[row][col] = num
                cnt_arr[num - 1] += 1
            else:
                arr[row][col] = num
                cnt_arr[num - 1] += 1

for cnt in cnt_arr:
    print(cnt)
