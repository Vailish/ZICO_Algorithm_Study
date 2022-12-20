for test_case in range(1, int(input()) + 1):
    N = int(input())
    maps = [input().split() for _ in range(N)]
    result = [[''] for _ in range(N)]
    print(f'#{test_case}')
    for _ in range(3):
        temp = [[''] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                temp[i][j] = maps[j][i]
            result[i] += temp[i][::-1]

        for idx in range(N):
            maps[idx] = temp[idx][::-1]

    for i in range(N):
        print(''.join(result[i][:N + 1]), ''.join(result[i][N + 1:2 * N + 1]), ''.join(result[i][2 * N + 1:]))
