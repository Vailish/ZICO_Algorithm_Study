# Boj_14696. 딱지놀
# https://www.acmicpc.net/problem/14696
# 14696. 딱지놀이

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count_a = [0] * 5
    count_b = [0] * 5
    result_arr = [0]
    for i in a[1:]:
        count_a[i] += 1
    for j in b[1:]:
        count_b[j] += 1

    for k in range(4, 0, -1):
        result = count_a[k] - count_b[k]
        if result == 0:
            if k == 1:
                winner = 'D'
                break
            continue
        elif result > 0:
            winner = 'A'
        else:
            winner = 'B'
        break
    print(winner)
