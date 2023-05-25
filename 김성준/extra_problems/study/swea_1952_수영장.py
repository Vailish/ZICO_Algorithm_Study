# swea_1952_수영장

for case in range(1, 1 + int(input())):
    daily_price, monthly_price, quarterly_price, yearly_price = map(int, input().split())
    plan = list(map(int, input().split()))

    cost = [[]for _ in range(13)]
    for month in range(1, 13):
        if month == 1:
            cost[1] = min(daily_price * plan[month-1],
                          monthly_price,
                          quarterly_price,
                          yearly_price)
        elif month == 2:
            cost[2] = min(daily_price * plan[month-1] + cost[month-1],
                          monthly_price + cost[1],
                          quarterly_price,
                          yearly_price)
        elif month == 3:
            cost[3] = min(daily_price * plan[month-1] + cost[month-1],
                          monthly_price + cost[2],
                          quarterly_price,
                          yearly_price)
        else:
            cost[month] = min(daily_price * plan[month-1] + cost[month-1],
                              monthly_price + cost[month-1],
                              quarterly_price + cost[month-3],
                              yearly_price)
    print(f'#{case}', cost[12])
