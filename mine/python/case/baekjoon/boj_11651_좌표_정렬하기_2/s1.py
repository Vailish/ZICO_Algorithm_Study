# 실버5 - 좌표 정렬하기2
# https://www.acmicpc.net/problem/11651

import sys


sys.stdin = open("input.txt")


def solution():
    lst = []
    for _ in range(int(input())):
        lst.append(tuple(map(int, input().split())))
    for a, b in sorted(lst, key=lambda x: (x[1], x[0])):
        print(a, b)


solution()
