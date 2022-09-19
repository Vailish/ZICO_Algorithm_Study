def sol():
    T = int(input())

    for test_case in range(1, T+1):
        print(f'#{test_case}', end=' ')
        time_list = list(map(int, input().split()))
        time = [0, 0]
        for i in range(len(time_list)):
            time[i % 2] += time_list[i]
        if time[1] >= 60:
            time[0] += time[1]//60
            time[1] %= 60
        time[0] %= 12
        if time[0] == 0:
            time[0] = 12
        print(*time)


sol()
