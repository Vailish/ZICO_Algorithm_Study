di = [-1,1,0,0]
dj = [0,0,-1,1]


def move():
    after_move = []
    for i in range(N):
        for j in range(N):
            # print(i,j)
            if maps[i][j]:
                # print(maps[i][j][0])
                amount, Dir = maps[i][j][0]
                # print(maps[i][j][0])
                dx = i + di[Dir]
                dy = j + dj[Dir]
                if dx in (0,N-1) or dy in (0,N-1):
                    amount //= 2
                    if amount == 0:
                        continue
                    Dir = Dir - 1 if Dir%2 else Dir + 1
                maps[i][j] = []
                after_move.append(((dx,dy),amount,Dir))

    for a in after_move:
        pos, amount, Dir = a
        maps[pos[0]][pos[1]].append((amount,Dir))


def cross_check():
    for i in range(N):
        for j in range(N):
            if len(maps[i][j]) > 1:
                total = 0
                max_mount = 0
                max_pos = 0
                for microbe in maps[i][j]:
                    total += microbe[0]
                    if max_mount < microbe[0]:
                        max_mount = microbe[0]
                        max_pos = microbe[1]
                maps[i][j] = [(total, max_pos)]


for tc in range(1,int(input())+1):
    N, M, K = map(int,input().split())  # N 맵크기 / M 진행시간 / K 군집개수
    maps = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        r, c, m, p = map(int,input().split())
        maps[r][c] = [(m, p-1)]
    for _ in range(M):
        move()
        cross_check()
    result = 0
    for i in range(N):
        print(maps[i])
        for j in range(N):
            if maps[i][j]:
                result += maps[i][j][0][0]
    print(f'#{tc} {result}')
    
# 50개중 42개만 정답