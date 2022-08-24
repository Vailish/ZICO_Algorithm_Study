for case in range(1, 1 + (int(input()))):
    N, M = map(int, input().split())

    # 파리수 담은 필드 만들기
    field = [list(map(int, input().split())) for _ in range(N)]

    # 파리채로 잡기
    kill_sum = 0
    kill_max = 0
    for i in range(N - M + 1):  # 검사할 i 범위
        for j in range(N - M + 1):  # 검사할 j 범위
            for num1 in range(i, i + M):  # 검사범위 안의 i
                for num2 in range(j, j + M):  # 검사범위 안의 j
                    kill_sum += field[num1][num2]
            if kill_max < kill_sum:
                kill_max = kill_sum
            kill_sum = 0
    print(f'#{case} {kill_max}')