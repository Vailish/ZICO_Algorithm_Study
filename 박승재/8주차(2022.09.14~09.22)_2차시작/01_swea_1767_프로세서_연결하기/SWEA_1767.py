import sys

sys.stdin = open('input.txt')


# d 방향에 코어가 있는지 확인하여 코어가 없으면 True를 반환 코어가 있으면 False를 반환
def chk_true(x, y, d):
    while True:
        x += dx[d]
        y += dy[d]
        if x in success or y in success:
            return True
        elif board[x][y] == 1:
            return False


# 코어 dfs
def dfs(t, c):
    global line, answer_line, answer_core
    # t가 리스트의 길이 즉 모든 코어를 다 돌았을때 값 저장
    if t == len(chk_list):
        if answer_core < c or answer_core == c and answer_line > line:
            answer_core = c
            answer_line = line
    else:
        x, y = chk_list[t]
        for d in range(4):
            # chk_true를 이용하여 해당하는 경로에 코어가 있는지 확인 코어가 없으면 진행
            if chk_true(x, y, d):
                nx, ny = x, y
                # board에 그대로 색칠
                while True:
                    nx += dx[d]
                    ny += dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        line += 1
                        board[nx][ny] = 1
                    else:
                        break
                # 연결된 코어 개수 + 1 후 다음 dfs
                dfs(t + 1, c + 1)
                nx, ny = x, y
                # dfs가 끝나고 색칠했던 부분 원상복구
                while True:
                    nx += dx[d]
                    ny += dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        line -= 1
                        board[nx][ny] = 0
                    else:
                        break
        # 해당 코어가 다른 코어들의 전선에 가로막혀 진행하지 못 하면
        # 연결된 코어 개수를 증가시키지 않고 다음 dfs
        dfs(t + 1, c)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    success = (-1, n)
    chk_list = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == 1:
                chk_list.append((i, j))
    answer = []
    answer_core = 0
    answer_line = n**2
    line = 0
    dfs(0, 0)
    print(answer_line)
