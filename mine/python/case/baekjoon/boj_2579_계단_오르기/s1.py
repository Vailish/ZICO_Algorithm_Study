# 계단 오르기 - silver 3
# https://www.acmicpc.net/problem/2579

def solution():
    n = int(input())
    stairs = []
    for i in range(n):
        stairs.append(int(input()))
    result = [0]*n

    for i in range(n):
        if i == 0:
            result[i] = stairs[i]
        elif i == 1:
            result[i] = stairs[i] + stairs[i-1]
        else:
            result[i] = max(
                result[i-3] + stairs[i-1] + stairs[i],
                result[i-2] + stairs[i]
            )

    print(result[-1])


solution()
