# 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD

# 60m 소요

import sys
sys.stdin = open('input.txt')

#############################################################
# 한 줄식 검사하자.                                         #
# 1. 한 열에 1 또는 2 한 종류만 있을 때 pass                #
# 2. 1과 2가 바뀌는 횟수를 카운트, 카운트한 값/2            #
# RB RB RB RB RB RB 6개의 교착상태 이지만, 바뀌는 횟수는 11 #
# 즉, 바뀌는 횟수가 N일 때, 교착상태는 (N + 1)/2 번이 됨.   #
# 이런 방법으로 전체 열을 다 돌아 합치면 결과가 땋!         #
# 처음과 끝에 각극이랑 반대되는 녀석이 있으면 필드에서 이탈 #
# 처음 수 받을 때랑, 다 끝낫을 때의 값을 보고 빼주기!       #
#############################################################

idx = {1: 2,
       2: 1}


def solution():
    result = []  # 매 열의 교착 수
    for j in range(100):
        cnt = 0  # 종류가 바뀔 때 카운트
        num = 0  # 현재의 숫자(1 또는 2)
        for i in range(100):
            # 처음 값 설정
            if field[i][j] != 0 and num == 0:
                num = field[i][j]
                if num == 2:  # 위 N극(1)이니까 다르면 빼주기
                    cnt -= 1
            # 다른 종류일 때 카운트 해주기
            elif num != 0 and field[i][j] == idx.get(num):
                cnt += 1
                num = field[i][j]
        if num == 1:  # 아래 S극(2)니까 다르면 빼주기
            cnt -= 1
        if cnt >= 1:
            cnt = (cnt + 1)//2
        result.append(cnt)
    return sum(result)


for case in range(1, 11):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case}', solution())
