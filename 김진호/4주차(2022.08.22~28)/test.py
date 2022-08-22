w, h = map(int,input().split())
for test_case in range(10):

                # 가로, 세로값 입력
    ant_x, ant_y = map(int,input().split())     # 개미 좌표 x,y 형식으로 입력 ( == 행열이 아니라 x,y 축으로 생각하자)
    dx = 1  # x축이동
    dy = 1  # y축이동
    stack = []
    start_x = ant_x
    start_y = ant_y
    cnt = 0

    while 1:
        ant_x += dx
        ant_y += dy
        cnt += 1
        if 0 < ant_x < w and 0 < ant_y < h:
            pass
        elif (ant_x == w or ant_x == 0) and not(ant_y == 0 or ant_y == h):
            dx *= -1
        elif (ant_y == h or ant_y == 0) and not(ant_x == w or ant_x == 0):
            dy *= -1
        else:
            dx *= -1
            dy *= -1

        if start_x == ant_x and start_y == ant_y and dx == 1 and dy == 1:
            print(cnt)
            break
        else:
            stack.append([ant_x, ant_y])