def sol():
    def spring_summer_winter():
        for i in range(n):
            for j in range(n):
                if tree[i][j]:
                    if K == 0:
                        tree[i][j].sort(reverse=True)
                    for z in range(len(tree[i][j]) - 1, -1, -1):
                        if board[i][j] >= tree[i][j][z]:
                            board[i][j] -= tree[i][j][z]
                            tree[i][j][z] += 1
                        else:
                            for die in tree[i][j][: z + 1]:
                                board[i][j] += die // 2
                            tree[i][j] = tree[i][j][z + 1 :]
                            break
                board[i][j] += add_vitamin[i][j]

    def autumn():
        for i in range(n):
            for j in range(n):
                for t in tree[i][j]:
                    if t % 5 == 0:
                        for d in range(8):
                            nx, ny = i + dx[d], j + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)

    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    n, m, k = map(int, input().split())
    board = [[5] * n for _ in range(n)]
    add_vitamin = [list(map(int, input().split())) for _ in range(n)]
    tree = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x, y, age = map(int, input().split())
        tree[x - 1][y - 1].append(age)

    for K in range(k):
        spring_summer_winter()
        autumn()
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += len(tree[i][j])

    print(answer)


sol()
