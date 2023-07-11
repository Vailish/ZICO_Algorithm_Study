# 2559. 수열

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

sum_temp = sum(temp[:k])
max_temp = sum_temp
for idx in range(n - k):
    sum_temp += temp[idx + k] - temp[idx]
    if max_temp < sum_temp:
        max_temp = sum_temp

print(max_temp)
