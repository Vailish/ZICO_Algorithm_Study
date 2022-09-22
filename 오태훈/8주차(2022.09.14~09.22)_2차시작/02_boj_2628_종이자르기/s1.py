# 2628. 종이자르기
# https://www.acmicpc.net/problem/2628

c, r = map(int, input().split())

n = int(input())

row_arr = [i for i in range(r)]
col_arr = [i for i in range(c)]
# rows, cols, r_cnt, c_cnt = [], [], 0, 0
rows, cols, r_cnt, c_cnt = [0], [0], 0, 0
for _ in range(n):
    cut, idx = map(int, input().split())
    if cut == 0:
        rows.append(idx)
    else:
        cols.append(idx)

rows.sort()
cols.sort()

rows.append(r)
cols.append(c)
max_r, max_c = 0, 0
for rr in range(1, len(rows)):
    rrr = rows[rr] - rows[rr - 1]
    if max_r < rrr:
        max_r = rrr
for cc in range(1, len(cols)):
    ccc = cols[cc] - cols[cc - 1]
    if max_c < ccc:
        max_c = ccc
print(max_c * max_r)

# --------------------------------------------

x, y = map(int, input().split())
n = int(input())

x_axis = [0]  # x축의 맨 왼쪽 값
y_axis = [0]  # y축의 맨 왼쪽 값

for _ in range(n):
    d, v = map(int, input().split())
    if d:  # d가 1인경우 (세로선)
        x_axis.append(v)
    else:  # d가 0인 경우 (가로선)
        y_axis.append(v)

x_axis.append(x)  # x축의 맨 오른쪽 값
y_axis.append(y)  # y축의 맨 오른쪽 값

x_axis.sort()  # 정렬 (순서대로 입력되지 않음)
y_axis.sort()  # 정렬 (순서대로 입력되지 않음)

x_value, y_value = [], []  # 간격을 저장하기 위한 변수
for idx, x in enumerate(x_axis[:-1]):  # 잘린 종이들의 길이 구하기
    x_value.append(x_axis[idx + 1] - x)
for idx, y in enumerate(y_axis[:-1]):  # 잘린 종이들의 길이 구하기
    y_value.append(y_axis[idx + 1] - y)

result = []  # 결과값을 저장하기 위한 리스트
for x in x_value:  # 각각의 x와 y값을 곱해서 리스트에 넣기
    for y in y_value:
        result.append(x * y)

print(max(result))  # 가장 큰 값 출력
