# swea_4008. [모의 SW 역량테스트] 숫자 만들기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH

import sys
sys.stdin = open('input.txt')


def dfs(depth, remains, value):
    global max_value, min_value
    # 종료조건
    if remains == [0, 0, 0, 0]:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    # 선택
    for i in range(4):  # +, -, *, /
        if remains[i] >= 1:
            new_remains = remains[:]
            new_remains[i] -= 1
            if i == 0:
                new_value = value + numbers[depth]
            elif i == 1:
                new_value = value - numbers[depth]
            elif i == 2:
                new_value = value * numbers[depth]
            else:  # i == 3:
                new_value = int(value // numbers[depth])
            dfs(depth + 1, new_remains, new_value)
            # 파이썬의 나누기(//)의 경우 나눈 결과 값이 23.4면 23을
            # -23.4면 -23이 아닌 -24를 결과값으로 주기 때문에 주의가 필요함!!
            # 음수 나누기 조심!!!!, 나머지를 버릴때는 항상 int로!
            # +1 해주는 방법은 정수값일 떄도 더해줘서 문제가 생길 수 있음



for case in range(1, 1 + int(input())):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_value = -100000000
    min_value = 100000000
    dfs(1, operator, numbers[0])
    print(f'#{case}', max_value - min_value)
