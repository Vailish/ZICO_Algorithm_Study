# 2527. 직사각형
# https://www.acmicpc.net/problem/2527

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # box1_x, box1_y = {x1, p1}, {y1, q1}
    # box2_x, box2_y = {x2, p2}, {y2, q2}
    box1_x, box1_y = set(range(x1, p1 + 1)), set(range(y1, q1 + 1))
    box2_x, box2_y = set(range(x2, p2 + 1)), set(range(y2, q2 + 1))

    chk_x = box1_x & box2_x
    chk_y = box1_y & box2_y

    x_len = len(chk_x)
    y_len = len(chk_y)
    if x_len > 1 and y_len > 1:
        result = 'a'
    elif x_len == 1 and y_len == 1:
        result = 'c'
    elif x_len == 1 or y_len == 1:
        result = 'b'
    else:
        result = 'd'
    print(result)
