total_map = [[0] * 1001 for _ in range(1001)]
n = int(input())
min_r, max_r = 1001, 0
for i in range(1, n + 1):
    c, r, w, h = map(int, input().split())
    for j in range(r, r + h):
        total_map[j][c:c + w] = [i] * w
    min_r, max_r = min(min_r, r), max(max_r, r + h)

for p in range(1, n + 1):
    result = 0
    for c in range(min_r, max_r):
        result += total_map[c].count(p)
    print(result)