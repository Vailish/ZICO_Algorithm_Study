def c(s1, s2):
    global min_v
    cnt = 0
    for i in range(s1):
        cnt += m - flag[i].count("W")
    for j in range(s1, s2):
        cnt += m - flag[j].count("B")
    for k in range(s2, n):
        cnt += m - flag[k].count("R")

    if min_v > cnt:
        min_v = cnt


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]
    min_v = 2500
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            c(i, j)

    print(f"#{tc + 1} {min_v}")