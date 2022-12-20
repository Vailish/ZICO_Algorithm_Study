for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    dx1, dx2 = min(x2, x4), max(x1, x3)
    dy1, dy2 = min(y2, y4), max(y1, y3)
    if dx1 == dx2 and dy1 == dy2:
        print('c')
    elif dx1 < dx2 or dy1 < dy2:
        print('d')
    elif dx1 > dx2 and dy1 > dy2:
        print('a')
    else:
        print('b')
