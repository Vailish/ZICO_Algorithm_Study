t = int(input())
for tc in range(t):
    n = int(input())
    numbers_list = [[0] * n for _ in range(n)]
    # 방향이 우 하 좌 상 순으로 반복
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 할당할 숫자 1~n^2 / 현재 위치 / 현재 진행 방향
    input_num = 1
    x, y = 0, 0
    now_dir = 0
    while input_num <= n**2:
        # 0, 0 시작점부터 1부터 숫자 대입
        numbers_list[x][y] = input_num
        input_num += 1

        # 현재 진행 방향으로 계속 이동이 가능한지 확인, 불가능하면 다음 진행방향으로 전환
        nx = x + dx[now_dir]
        ny = y + dy[now_dir]
        if (0 <= nx < n) and (0 <= ny < n) and (not numbers_list[nx][ny]):
            pass
        else:
            # 진행 방향 변경
            now_dir = (now_dir + 1) % 4

        # 진행가능한 방향으로 좌표 이동
        x = x + dx[now_dir]
        y = y + dy[now_dir]

    print(f"#{tc+1}")
    for i in range(n):
        print(*numbers_list[i])
