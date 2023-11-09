# 1, 2, 3 더하기 - silver3
# https://www.acmicpc.net/problem/9095

def solution():
    n = int(input())
    for _ in range(n):
        dp = [1, 2, 4]
        num = int(input())
        for i in range(3, num):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        print(dp[num-1])


solution()
