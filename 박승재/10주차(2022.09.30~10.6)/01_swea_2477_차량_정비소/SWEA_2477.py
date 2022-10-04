from collections import deque
import sys

sys.stdin = open("input.txt")


def sol():
    n, m, k, a, b = map(int, input().split())  # 접수, 정비, 고객, 사용한 창구번호들
    chk1 = list(map(int, input().split()))  # 접수 창구 시간
    chk1_bool = [[0, 0] for _ in range(n)]
    chk1_waiting_list = deque([])
    chk2 = list(map(int, input().split()))  # 정비 창구 시간
    chk2_bool = [0] * m
    chk2_waiting_list = deque([])
    clients = [0] + list(map(int, input().split()))
    clients_chk12 = [[0, 0] for _ in range(k + 1)]
    time = clients[1]
    answer = 0
    cnt = 0
    while cnt < k:
        if clients[-1] >= time:
            for i in range(1, k + 1):
                if clients[i] - time == 0:
                    chk1_waiting_list.append(i)
        for i in range(n):
            if chk1_bool[i][0] > 0:
                chk1_bool[i][0] -= 1
                if chk1_bool[i][0] == 0:
                    chk2_waiting_list.append(chk1_bool[i][1])
            if chk1_waiting_list and chk1_bool[i][0] == 0:
                client = chk1_waiting_list.popleft()
                chk1_bool[i] = [chk1[i], client]
                clients_chk12[client][0] = i + 1
        for i in range(m):
            if chk2_bool[i] > 0:
                chk2_bool[i] -= 1
            if chk2_waiting_list and chk2_bool[i] == 0:
                client = chk2_waiting_list.popleft()
                chk2_bool[i] = chk2[i]
                clients_chk12[client][1] = i + 1
                cnt += 1
                if clients_chk12[client] == [a, b]:
                    answer += client
        time += 1
    if answer == 0:
        print(-1)
        return
    print(answer)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    sol()
