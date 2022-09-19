T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}')

    # 달팽이의 크기 받기
    N = int(input())

    # 달팽이 집 생성
    house = [[0 for _ in range(N)] for _ in range(N)]
    house_number = 1

    # 달팽이 번호 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 달팽이 집 번호 시작 위치
    x = 0
    y = 0

    # 우하좌상 무한반복
    # 만약 house_number가 리스트의 크기와 같다면 반복 해제
    while True:
        for derection in range(4):
            while True:
                house[x][y] = house_number
                if 0 <= x+dx[derection] < N and 0 <= y+dy[derection] < N:
                    if house[x+dx[derection]][y+dy[derection]] == 0:
                        x += dx[derection]
                        y += dy[derection]
                        house_number += 1
                    else:
                        break
                else:
                    break
        if house_number == N*N:
            break

    for i in range(N):
        print(*house[i])
        