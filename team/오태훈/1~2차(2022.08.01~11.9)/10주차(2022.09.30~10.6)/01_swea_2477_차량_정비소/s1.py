# 2477. [모의 SW 역량테스트] 차량 정비소
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV6c6bgaIuoDFAXy

import sys
from collections import deque

sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    n, m, k, a, b = map(int, input().split())
    receipt = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    client = list(map(int, input().split()))
    c = client[:]
    times = [[] for _ in range(max(client) + 1)]
    for i, v in enumerate(client):
        times[v].append(i)
    time = 0
    rec = [-1] * n
    rep = [-1] * m
    wait = deque()
    wait2 = deque()
    end = []
    chk = [[] for _ in range(k)]
    while len(end) < k:
        for i, v in enumerate(rec):
            if v != -1:
                c[v] += 1
                if c[v] == client[v] + receipt[i]:
                    wait2.append(rec[i])
                    rec[i] = -1

        if time <= max(client):
            wait += times[time]

        while wait and -1 in rec:
            p = wait.popleft()
            idx = rec.index(-1)
            chk[p].append(idx)
            rec[idx] = p
            c[p], client[p] = time, time

        while wait2 and -1 in rep:
            p = wait2.popleft()
            idx = rep.index(-1)
            chk[p].append(idx)
            rep[idx] = p
            c[p], client[p] = time, time

        for i, v in enumerate(rep):
            if v != -1:
                c[v] += 1

                if c[v] == client[v] + repair[i]:
                    end.append(rec[i])
                    rep[i] = -1

        while wait2 and -1 in rep:
            p = wait2.popleft()
            idx = rep.index(-1)
            chk[p].append(idx)
            rep[idx] = p
            c[p], client[p] = time, time

        time += 1
    target = [a-1, b-1]
    cnt = 0
    for i in range(k):
        if chk[i] == target:
            cnt += i + 1
    if cnt == 0:
        cnt = -1
    print(f'#{t} {cnt}')
