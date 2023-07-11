# 1976. 시각 덧셈

for t in range(1, int(input()) + 1):
    h1, m1, h2, m2 = map(int, input().split())

    h = h1 + h2
    m = m1 + m2
    if m >= 60:
        m -= 60
        h += 1
    if h > 12:
        h -= 12
    print(f'#{t} {h} {m}')
