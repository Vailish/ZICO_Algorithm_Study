# 1211. [S/W 문제해결 기본] 2일차 - Ladder2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh

def find_path(row, col):
    cnt = 0
    status = 0                  # 이동 방향을 저장할 변수 (-1 : 오른쪽, 0 : 아래, 1: 왼쪽)
    while row < 99:             # 바닥에 도착할 때 까지
        while row < 99:         # 바닥에 도착할 때 까지
            row += dx[0]        # 아래로 이동
            col += dy[0]        # 아래로 이동
            cnt += 1            # 이동 거리 + 1
            if 99 > col and ladder[row][col + dy[1]]:   # 범위를 벗아나지 않고, 오른쪽이 1이면
                status = -1                             # 방향 설정
                break                                   # 반복 정지
            elif 0 < col and ladder[row][col + dy[2]]:  # 범위를 벗아나지 않고, 왼쪽이 1이면
                status = 1                              # 방향 설정
                break                                   # 반복 정지
        if status == -1:                                # 방향 변수가 오른쪽이면
            while True:
                row += dx[1]                            # 오른쪽으로 이동
                col += dy[1]
                cnt += 1                                # 이동거리 + 1
                if ladder[row + dx[0]][col]:            # 아래가 1이면지 정지
                    status = 0                          # 방향 설정
                    break
        elif status == 1:                               # 방향 변수가 왼쪽이면
            while True:
                row += dx[2]                            # 왼쪽으로 이동
                col += dy[2]
                cnt += 1
                if ladder[row + dx[0]][col]:            # 아래가 1이면 정
                    status = 0
                    break
    return cnt
dx = [1, 0, 0]                      # 아래, 오른쪽, 왼쪽
dy = [0, 1, -1]                     # 아래, 오른쪽, 왼쪽
for t in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10000
    for i in range(100):
        if ladder[0][i] == 1:       # 출발점 찾기
            cnt = find_path(0,i)    # 이동 거리 구하기
            if min_cnt >= cnt:      # 최소값, 인덱스 구하기
                min_cnt = cnt
                min_idx = i
    print(f'#{t} {min_idx}')