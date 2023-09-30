# 랜선자르기 - silver2
# https://www.acmicpc.net/problem/1654

import sys
sys.stdin = open("input.txt")


def solution():
    K, N = map(int, input().split())
    cables = []

    for _ in range(K):
        cables.append(int(input()))
    start_point = 1
    end_point = max(cables)

    while start_point <= end_point:
        middle_point = (start_point + end_point) // 2
        cnt = 0

        for cable in cables:
            cnt += cable//middle_point

        if cnt >= N:
            start_point = middle_point + 1
        else:
            end_point = middle_point - 1

    print(end_point)

    return


solution()
