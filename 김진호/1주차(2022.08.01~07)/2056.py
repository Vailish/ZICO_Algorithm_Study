mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for test_case in range(1, T + 1):
    ymd = input()
    year = int(ymd[0:4])
    month = int(ymd[4:6])
    day = int(ymd[6:8])

    if year != 0 and 0 < month <= 12:
        if mon_day[month - 1] >= day > 0:
            print(f'#{test_case} {ymd[0:4]}/{ymd[4:6]}/{ymd[6:8]}')
        else:
            print(f'#{test_case} -1')
    else:
        print(f'#{test_case} -1')
