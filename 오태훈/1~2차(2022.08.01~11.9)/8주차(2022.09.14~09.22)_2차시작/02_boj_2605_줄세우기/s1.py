# 2605. 줄 세우기
# https://www.acmicpc.net/problem/2605

n = int(input())
number = list(map(int, input().split()))

result = []
for i in range(n):
    result.insert(i - number[i], i + 1)
print(*result)
