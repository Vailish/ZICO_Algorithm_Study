from datetime import datetime

t = int(input())
for tc in range(t):
    m1, d1, m2, d2 = map(int, input().split())
    dt1 = datetime(2022, m1, d1)
    dt2 = datetime(2022, m2, d2)
    td = dt2 - dt1
    print(f"#{tc + 1} {td.days + 1}")
