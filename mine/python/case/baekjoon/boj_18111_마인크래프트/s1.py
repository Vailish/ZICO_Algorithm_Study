# 마인크래프트 - silver2
# https://www.acmicpc.net/problem/18111

# 제일 높은 곳을 깎아서 제일 낮은 곳에 넣어주기

import sys
sys.stdin = open("input.txt")


def solution():
    N, M, B = map(int, input().split())
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))

    print(field)


    return


solution()