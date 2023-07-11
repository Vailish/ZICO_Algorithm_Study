# 2383. [모의 SW 역량테스트] 점심 식사시간
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl

import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    person = []
    stairs = [0] * 11

    arr = [list(map(int , input().split())) for _ in range(n)]

    for row in range(n):
        for col in range(n):
            value = arr[row][col]
            if value == 1:
                person.append((row, col))
            elif value:
                stairs[value] = (row, col)
    print(person)
    print(stairs)

