# 4013. [모의 SW 역량테스트] 특이한 자석
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH

import sys

sys.stdin = open('input.txt')

# 자석 하나를 회전 시키는 함수
def turn(n, d):
    if d == 1:                                              # d == 1 일 때
        magnets[n] = [magnets[n][-1]] + magnets[n][:-1]     # 시계 방향으로 리스트 회전
    else:                                                   # d != 1 일 때
        magnets[n] = magnets[n][1:] + [magnets[n][0]]       # 반시계 방향으로 리스트 회전

# dfs? 자석들을 회전시키는 함수
def rotation(n, d):
    visited[n] = True                                       # 자석 방문 True
    turn(n, d)                                              # 회전
    d = -d                                                  # 방향 반대
    if (n + 1) < 4 and status[n] and not visited[n+1]:      # 범위, 회전 가능 상태, 방문 상태 고려
        rotation(n+1, d)                                    # 오른쪽 자석 회전
    if n-1 >= 0 and status[n-1] and not visited[n-1]:       # 범위, 회전 가능 상태, 방문 상태 고려
        rotation(n-1, d)                                    # 왼쪽 자석 회전


for t in range(1, int(input()) + 1):
    k = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(k):
        n, d = map(int, input().split())
        n -= 1
        status = []
        visited = [False] * 4                               # 방문 정보를 저장할 리스트
        for i in range(3):                                  # 자석과 자석 사이 == 3
            if magnets[i][2] != magnets[i+1][6]:            # 서로 극성이 다르면
                status.append(True)                         # True
            else:                                           # 극성이 같으면
                status.append(False)                        # Fasle
        rotation(n, d)                                      # 주어진 n번 자석 d방향 회전
    result = 0
    for score in range(4):                                  # 점수 계산
        result += magnets[score][0] * (2 ** score)
    print(f'#{t} {result}')

