# 1970. 쉬운 거스름돈 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq

import sys
sys.stdin = open('input.txt')


def solution(N):
    for i in range(len(cnt)):
        if value[i] <= N:
            cnt[i], N = divmod(N, value[i])

    return cnt


for case in range(1, 1+int(input())):
    N = int(input())  # 거슬러 주어야 할 금액
    cnt = [0] * 8
    value = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{case}')
    print(*solution(N))
