def sol():
    def move():
        for l in range(m):
            if sharks_location[l] != [-1, -1]:
                x, y = sharks_location[l]
                dir_li = direction[l][sharks_direction[l] - 1]
                for d in dir_li:
                    new_x, new_y = x + dx[d], y + dy[d]
                    if 0 <= new_x < n and 0 <= new_y < n and board[new_x][new_y] == 0:
                        sharks_location[l] = [new_x, new_y]
                        sharks_direction[l] = d
                        break
                else:
                    for d in dir_li:
                        new_x, new_y = x + dx[d], y + dy[d]
                        if 0 <= new_x < n and 0 <= new_y < n and board[new_x][new_y][0] == l + 1:
                            sharks_location[l] = [new_x, new_y]
                            sharks_direction[l] = d
                            break
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0:
                    if board[i][j][1] == 1:
                        board[i][j] = 0
                    else:
                        board[i][j][1] -= 1

    def kill():
        nonlocal sharks
        for l in range(m):
            if sharks_location[l] != [-1, -1]:
                if board[sharks_location[l][0]][sharks_location[l][1]] == 0 or board[sharks_location[l][0]][sharks_location[l][1]][0] == l + 1:
                    board[sharks_location[l][0]][sharks_location[l][1]] = [l + 1, k]
                else:
                    sharks_location[l] = [-1, -1]
                    sharks -= 1

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    sharks_location = [[] for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                sharks_location[board[i][j] - 1].extend([i, j])
                board[i][j] = [board[i][j], k]
    sharks_direction = list(map(int, input().split()))
    direction = [[] for _ in range(m)]
    for i in range(m):
        for _ in range(4):
            direction[i].append(list(map(int, input().split())))
    sharks = m
    answer = -1
    for ans in range(1, 1001):
        move()
        kill()
        if sharks == 1:
            answer = ans
            break

    print(answer)


sol()
