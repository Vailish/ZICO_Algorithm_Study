change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
money_cnt = [0] * 8
t = int(input())

for tc in range(t):
    n = int(input())
    for i in range(8):
        money_cnt[i] = n // change[i]
        n = n % change[i]

    print(f"#{tc + 1}")
    print(*money_cnt)
