T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    list_M = list(map(int, input().split()))
    MN_max = 0
    MN = 0
    if N > M:
        for idx in range(N - M + 1):
            for idx_M in range(0, M):
                MN += list_N[idx + idx_M] * list_M[idx_M]
            if MN_max < MN:
                MN_max = MN
            MN = 0

    elif M > N:
        for idx in range(M - N + 1):
            for idx_N in range(0, N):
                MN += list_N[idx_N] * list_M[idx + idx_N]
            if MN_max < MN:
                MN_max = MN
            MN = 0

    else:
        for idx in range(0, N):
            MN += list_N[idx] * list_M[idx]
        if MN_max < MN:
            MN_max = MN
        MN = 0

    print(f'#{test_case} {MN_max}')