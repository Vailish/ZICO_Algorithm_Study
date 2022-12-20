t = int(input())
for tc in range(t):
    p, q, r, s, w = map(int, input().split())
    cost1 = p * w
    cost2 = q
    if w > r:
        cost2 += (w - r) * s
    print(f"#{tc + 1} {min(cost1, cost2)}")
