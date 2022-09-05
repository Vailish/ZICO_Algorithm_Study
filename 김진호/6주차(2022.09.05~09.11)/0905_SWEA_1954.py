di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  # 우하좌상 순서 이동값
T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    snail_house = [[0]*size for _ in range(size)]
    move_direction = 0
    i = 0
    j = 0

    for turn in range(1, size*size+1):
        snail_house[i][j] = turn
        next_i = i+di[move_direction]
        next_j = j+dj[move_direction]
        if not(0 <= next_i <= size-1) or not(0 <= next_j <= size-1) or snail_house[next_i][next_j] != 0:
            move_direction = (move_direction + 1) % 4
            next_i = i + di[move_direction]
            next_j = j + dj[move_direction]
        i, j = next_i, next_j

    print(f'#{test_case}')
    for row in snail_house:
        print(*row)