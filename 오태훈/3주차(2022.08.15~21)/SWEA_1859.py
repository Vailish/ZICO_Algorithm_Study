# SWEA_1869. 백만 장자 프로젝트

for t in range(1, int(input()) + 1):
    n = int(input())
    costs = list(map(int, input().split()))
    revenue = 0
    # 코르트 리스트가 빌때까지 반복
    while costs:
        # 가격이 가장 비쌀 때를 찾는다.
        max_cost = max(costs)
        max_idx = costs.index(max_cost)
        # 그 전까지 구매 후 가장 가격이 비쌀 때 판다.
        revenue += max_idx * max_cost - sum(costs[:max_idx])
        # 지금까지 지난 가격 정보는 지운다.
        del costs[: max_idx + 1]
    print(f'#{t} {revenue}')
