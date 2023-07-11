import sys
sys.stdin = open("input.txt")

from collections import deque


M, N = map(int, input().split())
field = []
dq = deque()
switch = False
for i in range(N):
    lst = list(map(int, input().split()))
    if 1 in lst:
        for j in range(M):
            if lst[j] == 1:
                dq.append((i, j, 0))
            elif lst[j] == 0:
                switch = True
    field.append(lst)

visited = [[0] * M for _ in range(N)]
answer = -1
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while dq:
    r, c, d = dq.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not field[nr][nc]:
            field[nr][nc] = 1
            visited[nr][nc] = 1
            answer = max(answer, d+1)
            dq.append((nr, nc, d+1))
chk = 1
# 0(익지않는 토마토)이 있으면 -1 출력 그 외엔 1
for i in range(N):
    if 0 in field[i]:
        chk = 0

if chk == 1:  # 익지 않는 토마토가 없는 경우
    if not switch:  # 처음부터 익지않는 토마토가 없었던 경우
        print(0)
    else:
        print(answer)
else:  # 익지않는 토마토가 있는 경우
    print(-1)

