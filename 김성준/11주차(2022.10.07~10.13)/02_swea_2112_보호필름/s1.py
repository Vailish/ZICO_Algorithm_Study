# 2112. [모의 SW 역량테스트] 보호 필름
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu

import sys

sys.stdin = open('input.txt')


# 그냥 전부 탐색해!!!!!!
# 1. 그냥 통과하는지 검사 - 함수 만들기
# 2. r 개수를 for 문을 돌려서 하나씩 모든 경우 조사
#  -> 문제가 있는게 약품이 A, B 두가지... DFS 써서하는게 맘편할 듯


def search(arr):
    # 세로 검사
    for j in range(W):
        type = arr[0][j]
        cnt = 1
        for i in range(1, D):
            if arr[i][j] == type:
                cnt += 1
            else:
                type = arr[i][j]
                cnt = 1
            if cnt == K:
                break
        else:  # for 문을 break 해서 빠져 나왔다면 False
            return False

    return True


def dfs(arr, depth, ans):  # 현 상태배열, 행의 위치, 변경 횟수
    global result

    # 종료 조건
    if search(arr):
        result = min(result, ans)
        return

    # backtracking
    if ans == K or ans >= result or depth == D:
        return

    # 조건에 맞지 않는다면, 약품 써서 확인해주기!
    dfs(arr, depth + 1, ans)
    for change in [0, 1]:  # 0 = A약품, 1 = B약품
        tmp_lst = arr[:]
        if change == 0:
            tmp_lst[depth] = [0] * W
        elif change == 1:
            tmp_lst[depth] = [1] * W
        dfs(tmp_lst, depth + 1, ans + 1)


for case in range(1, 1 + int(input())):  # 정면을 볼 때, 가로 세로가 D, W
    D, W, K = map(int, input().split())  # D = 필름 두께, W = 가로크기, K = 합격기준
    arr = [list(map(int, input().split())) for _ in range(D)]
    result = K
    dfs(arr[:], 0, 0)
    print('#' + str(case), result)
