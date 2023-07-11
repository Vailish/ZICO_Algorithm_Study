def my_cul(t, p):
    if t == 0:
        return prices[t] * use[p], period[t]     # 요금, 기간 반환
    else:
        return prices[t], period[t]


def dfs(s, price):
    global min_v
    if s > 11:
        if price < min_v:
            min_v = price
        return
    if use[s]:
        for i in range(4):
            x, y = my_cul(i, s)
            dfs(s + y, price + x)
    else:
        dfs(s + 1, price)


t = int(input())
for tc in range(t):
    prices = list(map(int, input().split()))
    period = [1, 1, 3, 12]
    use = list(map(int, input().split()))
    min_v = prices[3]   # 1년짜리 끊었을 때로 초기화
    dfs(0, 0)
    print(f"#{tc + 1} {min_v}")