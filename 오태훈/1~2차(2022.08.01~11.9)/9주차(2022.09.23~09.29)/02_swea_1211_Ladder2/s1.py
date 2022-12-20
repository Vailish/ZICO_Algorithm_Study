# 1211. [S/W 문제해결 기본] 2일차 - Ladder2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh

def find_path(row, col):
    cnt = 0
    status = 0
    while row < 99:
        while row < 99:
            row += dx[0]
            col += dy[0]
            cnt += 1
            if 99 > col and ladder[row][col + dy[1]]:
                status = -1
                break
            elif 0 < col and ladder[row][col + dy[2]]:
                status = 1
                break
        if status == -1:
            while True:
                row += dx[1]
                col += dy[1]
                cnt += 1
                if ladder[row + dx[0]][col]:
                    status = 0
                    break
        elif status == 1:
            while True:
                row += dx[2]
                col += dy[2]
                cnt += 1
                if ladder[row + dx[0]][col]:
                    status = 0
                    break
    return cnt
dx = [1, 0, 0]
dy = [0, 1, -1]
for t in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10000
    for i in range(100):
        if ladder[0][i] == 1:
            cnt = find_path(0,i)
            if min_cnt >= cnt:
                min_cnt = cnt
                min_idx = i
    print(f'#{t} {min_idx}')