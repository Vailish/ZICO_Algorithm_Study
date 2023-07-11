# dp, memoization 사용해서 풀기
# dp는 부분결과를 이용해서 전체 결과를 구하는 방법

import sys
sys.stdin = open('input.txt')


def solution(plan, price):
    result = []
    for n in range(12):
        # 1월 까지의 최소 구하기
        if n != 0 and plan[n] == 0:
            result.append(result[n-1])
            continue
        if n == 0:  # 일, 달, 분기, 년
            result.append(min(plan[0] * price[0], price[1], price[2], price[3]))
        # 2, 3월까지의 최소 구하기
        elif n == 1 or n == 2:
            result.append(min(result[n-1] + plan[n] * price[0], result[n-1] + price[1], price[2], price[3]))
        # 4월 이후의 최소 구하기
        else:
            result.append(min(result[n-1] + plan[n] * price[0], result[n-1] + price[1], result[n-3] + price[2], price[3]))
    return result[11]


for case in range(1, 1 + int(input())):
    # 이용가격[일, 달, 분기, 년]
    price = list(map(int, input().split()))
    # 3개월권을 위해 추가
    plan = list(map(int, input().split()))
    print(f'#{case} {solution(plan, price)}')
