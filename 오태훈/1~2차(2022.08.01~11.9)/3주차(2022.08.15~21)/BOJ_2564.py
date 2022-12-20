# BOJ_2564. 경비원

w, h = map(int, input().split())
n = int(input())
arr = []
# 지도 생성 (False로 채우기)
map_arr = [[False] * (w + 1) for _ in range(h + 1)]
# 델타이동 상, 하, 좌, 우
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n + 1):
    d, l = map(int, input().split())

    if d == 1:
        row, col = 0, l
    elif d == 2:
        row, col = h, l
    elif d == 3:
        row, col = l, 0
    elif d == 4:
        row, col = l, w
    if i != n:
        # 상점은 2로 표시
        map_arr[row][col] = 2
    else:
        # 시작 위치 True
        map_arr[row][col] = True
check_arr = []
cnt = 0
d_idx = 0
# 모든 상점에 방문 하면 정지
while len(check_arr) < n:
    nr, nc = row + dr[d_idx][0], col + dr[d_idx][1]
    # 가장자리만 돌면서 값이 True가 아니면 진행하기
    if (
        0 <= nr < h + 1
        and 0 <= nc < w + 1
        and (nr == 0 or nr == h or nc == 0 or nc == w)
        and (map_arr[nr][nc] != True)
    ):
        row, col = nr, nc
        # 거리 + 1
        cnt += 1
        # 상점이 있으면
        if map_arr[row][col] == 2:
            # 지금까지 거리 배열에 추가
            check_arr.append(cnt)
        # 방문한 곳 True
        map_arr[nr][nc] = True
    d_idx += 1
    d_idx %= 4

sum_cnt = 0
for num in check_arr:
    # 거리가 최소값이 아닌경우
    if num > (w + h):
        # 최소값으로 변환
        num = 2 * (w + h) - num
    sum_cnt += num

print(sum_cnt)
