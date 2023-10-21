# 마인크래프트 - silver2
# https://www.acmicpc.net/problem/18111

# 제일 높은 곳을 깎아서 제일 낮은 곳에 넣어주기

import sys
from math import inf

sys.stdin = open("input2.txt")
input = sys.stdin.readline


def solution():
    N, M, B = map(int, input().split())
    field = []
    max_height = 0
    min_height = inf

    # 필드와 높이 범위 구하기
    for _ in range(N):
        lst = list(map(int, input().split()))
        field.append(lst)
        if max(lst) > max_height:
            max_height = max(lst)
        if min(lst) < min_height:
            min_height = min(lst)

    result = -1
    times = inf

    # 목표 높이마다 확인하기
    for target_height in range(max_height, min_height -1, -1):
        cnt = 0
        blocks = B

        # 목표 높이마다 걸리는 시간과 가능성 확인하기
        for i in range(N):
            for j in range(M):

                # 목표 높이 이상일 경우에 도달한 경우
                # 블럭을 파서 가방에 넣기
                if field[i][j] >= target_height:
                    cnt += (field[i][j] - target_height) * 2
                    blocks += (field[i][j] - target_height)

                # 목표 높이보다 작을 경우
                else:
                    # 해당 블럭만큼 빼서 채워넣어줌
                    cnt += (target_height - field[i][j])
                    blocks -= (target_height - field[i][j])

        # 사용한 블럭이 음수인 경우 패스
        if blocks < 0:
            continue

        # 결과값을 비교
        if times > cnt:
            times = cnt
            result = target_height

    print(times, result)


solution()
