for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(N)]
    tops = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > max_height:
                tops = []
                tops.append((i, j))
                max_height = maps[i][j]
            elif maps[i][j] == max_height:
                tops.append((i, j))

    while tops:
        top_idx_x, top_idx_y = tops.pop()
        stack = [(top_idx_x, top_idx_y, False)]
        while stack:
            x, y, usedig = stack.pop()
            for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= dx < N and 0 <= dy < N and visited[dx][dy]