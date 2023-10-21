# 집합 - 실버5
# https://www.acmicpc.net/problem/11723

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solution():
    S = set()
    M = int(input())
    for i in range(M):
        values = list(input().split())
        if len(values) == 1:
            if values[0] == "all":
                S = {i for i in range(1, 21)}
            else:
                S = set()
        else:
            type, val = values[0], int(values[1])
            if type == "add":
                if len(S) >= 20:
                    return
                S.add(val)
            elif type == "remove":
                if val in S:
                    S.remove(val)
            elif type == "check":
                if val in S:
                    print(1)
                else:
                    print(0)
            elif type == "toggle":
                if val in S:
                    S.remove(val)
                else:
                    S.add(val)
    return


solution()
