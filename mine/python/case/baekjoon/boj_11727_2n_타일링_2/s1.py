# boj11727 2*n 타일링 2 - silver3
# https://www.acmicpc.net/problem/11727
def solution():
    n = int(input())
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    print(dp[n]%10007)


solution()
