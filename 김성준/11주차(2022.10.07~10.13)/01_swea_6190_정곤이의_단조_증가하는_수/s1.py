# 6190. 정곤이의 단조 증가하는 수 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4


import sys
sys.stdin = open('input.txt')
#################################################
# 두 수를 뽑아 곱한다.                          #
# 단조 증가하는 수 인지 검사한다.               #
#  - 앞에서 부터 하나씩 빼서 검사한다.          #
# 단조 증가 한 수 중에서 곱이 최대값을 출력한다.#
#################################################
from itertools import permutations


def check(number):
    for i in range(0, len(number) - 1):
        if int(number[i]) > int(number[i+1]):
            return False
    return True


def solution():
    # 두 수를 뽑아 곱하기
    result = []
    for x, y in permutations(arr, 2):
        number = x * y
        # 단조 증가하는 수인지 검사
        if check(str(number)) == True:
            result.append(number)
    return max(result) if len(result) > 0 else -1


for case in range(1, 1 + int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{case}', solution())
