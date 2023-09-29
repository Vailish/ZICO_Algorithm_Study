# 덩치 - 실버4
# https://www.acmicpc.net/problem/7568

import sys


sys.stdin = open("input.txt")

# 1초에 최대 50명이기 때문에 시간초과 걱정은 없을 듯
# for문을 통해서 단순 비교를 통해서 진행하고, 결과값을 result에 담아두고
# result를 덩치 등수로 비교해주면 됨


def solution():
    N = int(input())
    men = []
    for _ in range(N):
        men.append(tuple(map(int, input().split())))

    # 덩치 비교하기
    result = []
    for num in range(len(men)):
        tmp = [num, 0]
        for man in men:
            if men[num][0] < man[0] and men[num][1] < man[1]:
                tmp[1] += 1
        tmp[1] += 1
        result.append(tmp)

    # 출력하기
    for i in range(N):
        print(result[i][1], end=" ")


solution()
