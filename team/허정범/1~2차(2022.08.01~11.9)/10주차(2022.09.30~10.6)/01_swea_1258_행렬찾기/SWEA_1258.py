def f(r, c):
    sr = r
    sc = c
    row = 1
    col = 1
    while True:     # row
        r += 1
        if r < n and arr[r][c]:
            row += 1
        else:
            r -= 1
            break

    while True:     # col
        c += 1
        if c < n and arr[r][c]:
            col += 1
        else:
            c -= 1
            break

    for m in range(sr, r + 1):
        for k in range(sc, c + 1):
            arr[m][k] = 0

    return [row, col]


t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                result.append(f(i, j))

    result = sorted(result, key=lambda x: (x[0]*x[1], x[0]))
    print(f'#{tc + 1} {len(result)}', end=' ')
    for line in result:
        print(*line, end=' ')
    print()
