# 1952. [모의 SW 역량테스트] 수영장

# DP

for t in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))                # 이용권 가격들
    plan = list(map(int, input().split()))                  # 12개월 이용 계획
    total_cost = [0] * 13                                   # 총 비용을 저장할 리스트
    for i in range(1, 13):
        day_cost = plan[i - 1] * prices[0]                  # 1일 이용권을 이용했을 때의 가격
        month_cost = prices[1]                              # 1달 이용권을 이용했을 때의 가격
        day_or_month = min(day_cost, month_cost)            # 1달 이용권과 1일 이용권중 더 저렴한 가격
        total_cost[i] = total_cost[i - 1] + day_or_month    # 지금까지의 누적하여 리스트에 더하기
        if i >= 3:                                          # 3월 이상일 때 3개월권 사용 가능
            month_3 = (
                total_cost[i - 3] + prices[2]
            )                                               # 1일권 / 1달권 비교한 누적값 , 3개월전 누적값  + 3개월권
            total_cost[i] = min(total_cost[i], month_3)     # 더 작은 값을 리스트에 저장
    year_or_total = min(prices[3], total_cost[12])          # 최종 누적값과 1년권의 가격 비교
    print(f'#{t} {year_or_total}')

# DFS

def dfs(cost, month):
    global min_cost
    if month > 12:                                  # 12월까지 계산했을 때
        min_cost = min(min_cost, cost)              # 최소 값은 1일, 1달, 3달 계산값과 1년권중 저렴한 가격
        return                                      # 재귀 탈츨
    dfs(cost + plan[month] * prices[0], month + 1)  # 1일권 계산
    dfs(cost + prices[1], month + 1)                # 1달권 계산
    dfs(cost + prices[2], month + 3)                # 3달권 계산


for t in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))        # 이용권 가격들
    plan = [0] + list(map(int, input().split()))    # 12개월 이용 계획
    min_cost = prices[3]                            # 1년권 가격을 가장 저렴한 비용에 저장
    dfs(0, 1)                                       # 0원, 1월로 dfs 시작
    print(f'#{t} {min_cost}')
