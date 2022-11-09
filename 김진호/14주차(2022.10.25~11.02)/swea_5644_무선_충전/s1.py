# d = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
d = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
for tc in range(1, int(input())+1):
    M, A = map(int, input().split())
    path_a = list(map(int, input().split()))
    path_b = list(map(int, input().split()))
    BCs = [list(map(int, input().split())) for _ in range(A)]
    BCs.sort(key=lambda t: t[3])
    BC_map = [[[(-1, 0)] for _ in range(11)] for _ in range(11)]
    for i, BC in enumerate(BCs):
        x, y, dis, power = BC
        stack = [(x, y, 0)]
        visited = [[False] * 11 for _ in range(11)]
        BC_map[x][y].insert(0, (i, power))
        visited[x][y] = True
        while stack:
            x, y, k = stack.pop(0)
            # x, y, k = stack.pop()
            for dx, dy in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                if 0 < dx <= 10 and 0 < dy <= 10 and not visited[dx][dy]:
                    BC_map[dx][dy].insert(0, (i, power))
                    visited[dx][dy] = True
                    if k+1 < dis:
                        stack.append((dx, dy, k+1))
    result = 0
    ax, ay = 1, 1
    bx, by = 10, 10
    for act in range(M):
        a_BC = BC_map[ax][ay]
        b_BC = BC_map[bx][by]
        if a_BC[0][0] == -1 and b_BC[0][0] == -1:
            pass
        elif a_BC[0][0] == b_BC[0][0]:
            result += max(a_BC[0][1], a_BC[0][1] + b_BC[1][1], a_BC[1][1] + b_BC[0][1])
        else:
            result += a_BC[0][1]
            result += b_BC[0][1]

        ax += d[path_a[act]][0]
        ay += d[path_a[act]][1]
        bx += d[path_b[act]][0]
        by += d[path_b[act]][1]
    a_BC = BC_map[ax][ay]
    b_BC = BC_map[bx][by]
    if a_BC[0][0] == -1 and b_BC[0][0] == -1:
        pass
    elif a_BC[0][0] == b_BC[0][0]:
        result += max(a_BC[0][1], a_BC[0][1] + b_BC[1][1], a_BC[1][1] + b_BC[0][1])
    else:
        result += a_BC[0][1]
        result += b_BC[0][1]
    print(f'#{tc} {result}')
