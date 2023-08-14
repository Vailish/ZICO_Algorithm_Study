# 적록색약 - Gold5
# https://www.acmicpc.net/problem/10026


# 코드가 너무 지저분해서 한 번 정리해보자! s2 gogo!

import sys


sys.stdin = open("input.txt")
sys.setrecursionlimit(2500)


def solution():

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 일반인 dfs
    def general_dfs(start_r, start_c, color):
        r, c = start_r, start_c
        general_visited[r][c] = 1
        # 델타 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not general_visited[nr][nc] and field[nr][nc] == color:
                general_dfs(nr, nc, color)

    def special_dfs(start_r, start_c, color):
        r, c = start_r, start_c
        special_visited[r][c] = 1

        # 델타 이동
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]

            if color == "R" or color == "G":
                if 0 <= nr < n and 0 <= nc < n and not special_visited[nr][nc] and (field[nr][nc] == "R" or field[nr][nc] == "G"):
                    special_dfs(nr, nc, color)
            else:
                if 0 <= nr < n and 0 <= nc < n and not special_visited[nr][nc] and field[nr][nc] == color:
                    special_dfs(nr, nc, color)

    # input 값들을 filed라는 2차원 배열로 만들어 준다
    n = int(input())

    #  전역변수 설정
    field = []

    for _ in range(n):
        field.append(input())

    # visited 설정
    general_visited = [[0] * n for _ in range(n)]
    special_visited = [[0] * n for _ in range(n)]

    general_count = 0
    special_count = 0

    # 모든 곳에서 dfs를 돌려봄
    # 일반 기준으로
    for i in range(n):
        for j in range(n):
            if general_visited[i][j]:
                continue
            general_dfs(i, j, field[i][j])
            general_count += 1

    # 적록색약 기준으로
    for i in range(n):
        for j in range(n):
            if special_visited[i][j]:
                continue
            special_dfs(i, j, field[i][j])
            special_count += 1

    # 해당 값들을 출력해주기
    print(general_count, special_count)


solution()
