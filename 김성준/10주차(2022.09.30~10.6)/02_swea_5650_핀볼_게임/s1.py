# 5650. [모의 SW 역량테스트] 핀볼 게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo


import sys
sys.stdin = open('input.txt')

# 0번은 버리고, 상 하 좌 우 일 때 공의 방향(dx, dy)
block = [
    [],  # 0
    [(1, 0), (0, 1), (0, -1), (-1, 0)],  # 1
    [(0, 1), (-1, 0), (0, -1), (1, 0)],  # 2
    [(0, -1), (-1, 0), (1, 0), (0, 1)],  # 3
    [(1, 0), (0, -1), (-1, 0), (0, 1)],  # 4
    [(1, 0), (-1, 0), (-1, 0), (0, 1)]]  # 5


# 상(0) 하(1) 좌(2) 우(3)
direction_idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # dx, dy


# 델타 이동을 통해서 해보자!
def solution():
    # 웜홀 정보 기입
    for i in range(N):
        for j in range(N):
            if field[i][j] in [6, 7, 8, 9, 10]:
                worm[field[i][j]].append((i, j))

    result = []  # 모든 경우의 점수 저장
    for i in range(N):
        for j in range(N):
            if field[i][j] == 0:
                x, y = i, j
                # 시작 지점 설정 후 시작!
                for direction in range(4):
                    dx = [-1, 1, 0, 0][direction]  # 상 하 좌 우
                    dy = [0, 0, -1, 0][direction]
                    nx, ny = x, y
                    score = 0
                    # 게임 시작
                    while field[nx][ny] != -1:
                        # 벽 만날 때 까지 쭉 직진!
                        while 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 0:
                            nx += dx
                            ny += dy

                        # 웜홀을 만난 경우
                        if field[nx][ny] in [6, 7, 8, 9, 10]:
                            for idx in worm[field[nx][ny]]:
                                if (nx, ny) != idx:
                                    nx, ny = idx
                                    continue
                        # 모서리인 경우
                        if (nx == 0 and dx == -1) or (nx == N and dx == 1):
                            nx -= dx
                            dx *= -1
                            score += 1
                            continue
                        elif (ny == 0 and dy == -1) or (ny == N and ny == 1):
                            ny -= dy
                            dy *= -1
                            score += 1
                            continue

                        # 벽을 만났을 경우, 0과 N이 아니므로
                        if field[nx][ny] in [1, 2, 3, 4, 5]:
                            dx, dy = block[field[nx][ny]][direction_idx.get((dx, dy))]
                            score += 1
                    result.append(score)

    return max(result)


for case in range(1, 1 + int()):
    N = int(input())  # 한 변의 길이
    field = list(map(int, input().split()))
    worm = [[] for _ in range(11)]
    print(f'#{case}', solution())
