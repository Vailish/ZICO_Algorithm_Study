# 2112. [모의 SW 역량테스트] 보호 필름
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu

import sys
sys.stdin = open('input.txt')

import

# 그냥 전부 탐색해!!!!!!
# 1. 그냥 통과하는지 검사 - 함수 만들기
# 2. r 개수를 for 문을 돌려서 하나씩 모든 경우 조사
#  -> 문제가 있는게 약품이 A, B 두가지... DFS 써서하는게 맘편할 듯

def search(arr):
    films = arr[:]
    # 세로 검사
    for i in range(D):
        type = films[i][0]
        cnt = 1
        for j in range(W):
            if cnt >= K:
                return False  # 출력 0

            if films[i][j] == type:
                cnt += 1
            else:
                type = films[i][j]
                cnt = 1
    return True


def dfs(arr, depth):
    # 종료 조건
    if search(arr):
        return depth



def solution():
    films = arr[:]
    # 바로 성립하는 경우
    if not search(films):
        return 0

    dfs(arr, 0)
    return


for case in range(1, 1 + int(input())):  # 정면을 볼 때, 가로 세로가 D, W
    D, W, K = map(int, input().split())  # D = 필름 두께, W = 가로크기, K = 합격기준
    arr = [list(map(int, input().split())) for _ in range(D)]
    print('#' + str(case), solution())
