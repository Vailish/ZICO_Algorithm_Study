from itertools import combinations



N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

for factors in combinations(sorted(nums), 3):
    if sum(factors) == M:
        result = M
        break
    elif sum(factors) < M:
        result = max(sum(factors), result)

print(result)
