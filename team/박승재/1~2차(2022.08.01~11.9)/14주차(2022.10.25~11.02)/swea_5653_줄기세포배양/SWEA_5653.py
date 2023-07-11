def sol():
    def painting(v, x, y):
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) not in visit:
                visit.add((nx, ny))
                disable.append([v, v, nx, ny])

    def process():
        for i in range(len(disable) - 1, -1, -1):
            if disable[i][0] == 1:
                able.append([disable[i][1] + 1] + disable[i][1:])
                del disable[i]
            else:
                disable[i][0] -= 1

        if able:
            able.sort(key=lambda x: (x[1], x[0]))
            for i in range(len(able) - 1, -1, -1):
                if able[i][0] == able[i][1]:
                    painting(able[i][1], able[i][2], able[i][3])
                if able[i][0] == 1:
                    del able[i]
                else:
                    able[i][0] -= 1

        return

    for tc in range(1, int(input()) + 1):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n, m, k = map(int, input().split())
        disable, able, visit = [], [], set()
        for i in range(n):
            li = list(map(int, input().split()))
            for j in range(m):
                if li[j] > 0:
                    visit.add((i, j))
                    disable.append([li[j], li[j], i, j])
        for _ in range(k):
            process()

        print('#{} {}'.format(tc, len(disable) + len(able)))


sol()
