# BOJ_10158. 개미


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p += t % (2 * w)
q += t % (2 * h)
# 범위를 벗어남
if p > w:
    p -= w
    p = w - p
    if p < 0:
        p *= -1
if q > h:
    q -= h
    q = h - q
    if q < 0:
        q *= -1

print(p, q)
