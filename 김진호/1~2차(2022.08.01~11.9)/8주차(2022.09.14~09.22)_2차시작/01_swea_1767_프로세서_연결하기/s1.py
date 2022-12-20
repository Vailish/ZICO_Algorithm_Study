import sys
sys.stdin = open("input.txt")


def find_road(core_idx, visit_case):
    global min_path
    if core_idx == len(cores):
        cnt = 0
        for i in range(N):
            for j in range(N):
                if visit_case[i][j]:
                    cnt += 1
        cnt -= core_cnt
        if min_path > cnt:
            min_path = cnt
        return

    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        path = []
        di = cores[core_idx][0] + dx
        dj = cores[core_idx][1] + dy
        if (di == 0 or di == N - 1 or dj == 0 or dj == N - 1) and not visit_case[di][dj]:
            visit_case[di][dj] = True
            find_road(core_idx + 1, visit_case)
            visit_case[di][dj] = False
            continue
        if 0 < di < N - 1 and 0 < dj < N - 1 and not visit_case[di][dj]:
            path.append((di, dj))
            while 1:
                di += dx
                dj += dy
                if (di == 0 or di == N - 1 or dj == 0 or dj == N - 1) and not visit_case[di][dj]:
                    for p in path:
                        visit_case[p[0]][p[1]] = True
                    visit_case[di][dj] = True
                    find_road(core_idx + 1, visit_case)
                    for p in path:
                        visit_case[p[0]][p[1]] = False
                    visit_case[di][dj] = False
                    break
                if 0 < di < N - 1 and 0 < dj < N - 1 and not visit_case[di][dj]:
                    path.append((di, dj))
                else:
                    break


for test_case in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    core_cnt = 0
    visit = [[False] * N for _ in range(N)]
    min_path = N * N

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                cores.append((i, j))
                visit[i][j] = True
                core_cnt += 1
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    cores.pop()

    find_road(0, visit)
    if min_path == N * N:
        min_path = 0
    print(f'#{test_case} {min_path}')

print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
