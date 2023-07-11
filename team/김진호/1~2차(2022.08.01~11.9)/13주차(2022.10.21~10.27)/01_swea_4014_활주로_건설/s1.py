def chk(i,j):
    if j+1 < N:
        if maps[i][j] == maps[i][j + 1] - 1:
            for airstrip in range(j, j - X, -1):
                if 0 <= airstrip < N and not visited[airstrip]:
                    visited[airstrip] = True
                else:
                    return False
        elif maps[i][j] < maps[i][j + 1] - 1:
            return False

    if j-1 >= 0:
        if maps[i][j] == maps[i][j - 1] - 1:
            for airstrip in range(j, j + X):
                if 0 <= airstrip < N and not visited[airstrip]:
                    visited[airstrip] = True
                else:
                    return False
        elif maps[i][j] < maps[i][j - 1] - 1:
            return False
    return True


def chk2(i,j):
    if i+1 < N:
        if maps[i][j] == maps[i+1][j] - 1:
            for airstrip in range(i, i - X, -1):
                if 0 <= airstrip < N and not visited[airstrip]:
                    visited[airstrip] = True
                else:
                    return False
        elif maps[i][j] < maps[i+1][j] - 1:
            return False

    if i-1 >= 0:
        if maps[i][j] == maps[i-1][j] - 1:
            for airstrip in range(i, i + X):
                if 0 <= airstrip < N and not visited[airstrip]:
                    visited[airstrip] = True
                else:
                    return False
        elif maps[i][j] < maps[i-1][j] - 1:
            return False
    return True


for tc in range(1,int(input())+1):
    N, X = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    cnt = 0
    for i in range(N):
        visited = [False] * N
        cnt = 0
        for j in range(N):
            if not chk(i,j):
                break
        else:
            result += 1

    for j in range(N):
        visited = [False] * N
        cnt = 0
        for i in range(N):
            if not chk2(i,j):
                break
        else:
            result += 1

    print(f'#{tc} {result}')
