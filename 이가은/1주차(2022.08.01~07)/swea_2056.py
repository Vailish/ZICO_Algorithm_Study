t = int(input())

for test_case in range(1, t + 1):
    numbers = input()
    year = numbers[:4]
    month = numbers[4:6]
    date = numbers[6:]
    if month in ('01', '03', '05', '07', '08', '10', '12') and '01' <= date <= '31':
        print(f'#{test_case} {year}/{month}/{date}')
    elif month in ('04', '06', '09', '11') and '01' <= date <= '30':
        print(f'#{test_case} {year}/{month}/{date}')
    elif month == '02' and '01' <= date <= '28':
        print(f'#{test_case} {year}/{month}/{date}')

    else:
        print(f'#{test_case} -1')
