# 2×n 타일링 silver3
# https://www.acmicpc.net/problem/11726


def solution():
    n = int(input())
    dp = [0, 1, 2]

    if n <= 2:
        print(dp[n])
        return

    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])

    print(dp[n]%10007)


solution()
