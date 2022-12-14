def move(x, y, h):
    visit[x][y] = True
    global long_way, flag
    road.append(road_map[x][y])
    if long_way < len(road):
        long_way = len(road)
    for n in range(4):
        mx = x + dx[n]
        my = y + dy[n]
        if 0 <= mx < N and 0 <= my < N and not visit[mx][my] and road_map[mx][my] < h:
            move(mx, my, road_map[mx][my])
        elif (
            flag
            and 0 <= mx < N
            and 0 <= my < N
            and not visit[mx][my]
            and road_map[mx][my] - K < h
        ):
            flag = False
            move(mx, my, h - 1)
            flag = True
    road.pop()
    visit[x][y] = False


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    N, K = map(int, input().split())

    road_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]

    higest_h = 0

    for chk in road_map:
        if higest_h < max(chk):
            higest_h = max(chk)

    long_way = 0
    for i in range(N):
        for j in range(N):
            if road_map[i][j] == higest_h:
                flag = True
                road = []
                move(i, j, higest_h)
    print(long_way)
