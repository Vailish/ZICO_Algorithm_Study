dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def active(x, y, life):

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not new[nx][ny]:
            new[nx][ny] = life
            start.append([nx, ny, life])
        else:
            if new[nx][ny] < life:
                new[nx][ny] = life


for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    new = [[0]*(m+k) for _ in range(n+k)]
    start = []

    # 미생물 새로운 이차원배열에 다시 배치
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                new[i+k//2][j+k//2] = arr[i][j] * 2 - 1
                start.append([i+k//2, j+k//2], arr[i][j])

    for time in range(1, k+1):
        for cell in start:
            for x, y, life in cell:
                new[x][y] -= 1
                if new[x][y] == life:
                    active(x,y, life)