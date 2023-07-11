import sys
from collections import deque
input = sys.stdin.readline


def turn(line):
    for l in line:
        if l != 0:
            l2 = 2**l
            board1 = [[] for _ in range(N2)]
            for n in range(0, N2, l2):
                for j in range(N2):
                    for i in range(l2 - 1, -1, -1):
                        board1[j % (l2) + n].append(board[i + n][j])
        else:
            board1 = [item[:] for item in board]
        melt(board1)
    return


def melt(board2):
    global board
    board = [item[:] for item in board2]
    for i in range(N2):
        for j in range(N2):
            if board2[i][j] > 0:
                cnt = 0
                for n in range(len(dx)):
                    mx, my = i + dx[n], j + dy[n]
                    if 0 <= mx < N2 and 0 <= my < N2 and board2[mx][my] > 0:
                        cnt += 1
                    if cnt == 3:
                        break
                if cnt < 3:
                    board[i][j] -= 1
    return


def chk(i, j):
    cnt = 0
    queue = deque([(i, j)])
    visit.add((i, j))
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for n in range(len(dx)):
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < N2 and 0 <= my < N2 and board[mx][my] != 0 and (mx, my) not in visit:
                visit.add((mx, my))
                queue.append((mx, my))
    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, Q = map(int, input().split())
N2 = 2**N
board = [list(map(int, input().split())) for _ in range(N2)]
visit = set()
L = list(map(int, input().split()))
turn(L)
highest_cnt = 0
total = 0
for i in range(N2):
    for j in range(N2):
        total += board[i][j]
        if board[i][j] != 0 and (i, j) not in visit:
            cnt = chk(i, j)
            if highest_cnt < cnt:
                highest_cnt = cnt
print(total)
print(highest_cnt)



