# 1954. 달팽이 숫자
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq


def find(i, j):
    global row, col, cnt, number, snail, end_condition, N
    while cnt < N - 1 and snail[row + i][col + j] == 0:
        number += 1
        if i != 0:
            row += i
        else:
            col += j
        snail[row][col] = number
        end_condition = 0
        cnt += 1
    cnt = 0


T = int(input())
for t in range(1, T + 1):

    # 다음에 입력할 곳의 값이 0이면 계속 0 이 아니면 스탑
    N = int(input())
    snail = [[0 for j in range(N)] for i in range(N)]  # 0으로 채워져 있는 2차원 배열 선언
    snail[0][0] = 1  # 0,0에 1 할당
    number = 1  # 할당해줄 숫자
    row, col, cnt, end_condition = 0, 0, 0, 0
    while number != N**2:  # number가 N의 제곱이 될 때까지 반복
        find(0, 1)  # 오른쪽 탐색, 채우기
        find(1, 0)  # 아래쪽 탐색, 채우기
        find(0, -1)  # 왼쪽 탐색, 채우기
        find(-1, 0)  # 위쪽 탐색, 채우기
    print(f'#{t}')
    for rows in snail:
        for cols in rows:
            print(cols, end=' ')
        print()
