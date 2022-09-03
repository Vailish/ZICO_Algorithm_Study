t = int(input())
for tc in range(t):
    h1, m1, h2, m2 = map(int, input().split())

    h = (h1 + h2 + ((m1 + m2) // 60)) % 12
    m = (m1 + m2) % 60
    if h == 0:
        h = 12

    print(f"#{tc + 1} {h} {m}")
