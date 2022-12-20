import copy

dr = [0, 0, 1]  # 좌 우 하
dc = [-1, 1, 0]


for _ in range(10):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    start = list(filter(lambda x: matrix[0][x] == 1, range(100)))
    cnt_list = []
    for s in start:
        temp = copy.deepcopy(matrix)
        cnt = 0
        r, c = 0, s
        while r < 99:
            temp[r][c] = 0
            cnt += 1
            for d in range(3):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < 100 and 0 <= nc < 100 and temp[nr][nc] == 1:
                    r, c = nr, nc
                    break
        cnt_list.append(cnt)
    result = cnt_list[::-1].index(min(cnt_list))
    print(f"#{n} {start[::-1][result]}")