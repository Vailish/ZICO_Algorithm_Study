# 4613. 러시아 국기 같은 깃발 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj


###################################
# 세로 축을 3분할 하여            #
# 바꿔야 할 색들을 저장하여       #
# 그 중 최소가 되는 값을 출력한다.#
###################################

import sys
sys.stdin = open('input.txt')


def solution():
    result = []  # 각 경우의 값 저장
    # 세로 축을 3분할 하여
        # (0,k), (k,l), (l,N) -> i,
    for k in range(0, N-2):  # k까지 = 흰, W
        for l in range(k+1, N-1):  # k+1 ~ l까지 = 파, B | 나머지 R

            cnt = [0] * 3  # 각각 W, B, R
        # 1) W 부분
            for i in range(0, k+1):
                for j in range(M):
                    if flag[i][j] != 'W':   # count method
                        cnt[0] += 1
        # 2) B 부분
            for i in range(k+1, l+1):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cnt[1] += 1
        # 3) R 부분
            for i in range(l+1, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cnt[2] += 1
            result.append(sum(cnt))
    return min(result)


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 가로, M = 세로
    flag = [input() for _ in range(N)]
    print(f'#{case}', solution())
