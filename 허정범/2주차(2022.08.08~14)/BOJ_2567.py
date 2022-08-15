t = int(input())
# 델타이동
d_row = [0, -1, 0, 1]
d_col = [1, 0, -1, 0]
map_list = [[0] * 100 for _ in range(100)]
overlap_cnt = 0
for tc in range(t):
    col, row = map(int, input().split())
    for i in range(row, row + 10):
        for j in range(col, col + 10):
            if map_list[i][j]:
                overlap_cnt += 1
                continue
            map_list[i][j] = 1

len_cnt = 0
for l in range(100):
    for m in range(100):
        if map_list[l][m]:
            for delta_idx in range(4):
                nl = l + d_row[delta_idx]
                nm = m + d_col[delta_idx]
                if 0 <= nl < 100 and 0 <= nm < 100 and (not map_list[nl][nm]):
                    len_cnt += 1
                elif nl in (-1, 100) or nm in (-1, 100):
                    len_cnt += 1
print(len_cnt)
