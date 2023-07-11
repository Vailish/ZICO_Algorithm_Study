N = int(input())
list_p = [list(map(int, input().split())) for _ in range(N)]

list_p_size = 100 * N

for idx in range(N - 1):
    for idx_2 in range(idx + 1, N):
        if (
            abs(list_p[idx][0] - list_p[idx_2][0]) < 10
            and abs(list_p[idx][1] - list_p[idx_2][1]) < 10
        ):
            list_p_size -= (10 - abs(list_p[idx][0] - list_p[idx_2][0])) * (
                10 - abs(list_p[idx][1] - list_p[idx_2][1])
            )
print(list_p_size)
