# 적록색약 - Gold5
# https://www.acmicpc.net/problem/10026


# s1에서 input 받을 때 적록색약용을 하나 만들고서 하나의 dfs로 돌리는 방법으로 진행!
# 결과 165128KB	280ms 에서 153048KB	248ms로 향상

import sys


sys.stdin = open("input.txt")
sys.setrecursionlimit(5000)


def solution():

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # dfs
    def dfs(start_r, start_c, color):
        r, c = start_r, start_c
        visited[r][c] = 1
        # 델타 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and field[nr][nc] == color:
                dfs(nr, nc, color)

    # input 값들을 filed라는 2차원 배열로 만들어 준다
    n = int(input())

    # 변수 설정
    field = []
    field_m = []

    for _ in range(n):
        str = input()
        field.append(str)

        tmp = ""
        for c in str:
            if c == "G":
                tmp += "R"
            else:
                tmp += c
        field_m.append(tmp)

    # visited 설정
    visited = [[0] * n for _ in range(n)]

    general_count = 0
    special_count = 0

    # 모든 곳에서 dfs를 돌려봄
    # 일반 기준으로
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            dfs(i, j, field[i][j])
            general_count += 1

    # visited 초기화
    visited = [[0] * n for _ in range(n)]
    field = field_m[:]

    # 적록색약 기준으로
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            dfs(i, j, field[i][j])
            special_count += 1

    # 해당 값들을 출력해주기
    print(general_count, special_count)


solution()
