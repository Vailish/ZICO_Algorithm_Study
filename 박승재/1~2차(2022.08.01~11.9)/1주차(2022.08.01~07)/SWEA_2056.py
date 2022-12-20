T = int(input())
for t in range(1, 1 + T):
    input_day = input()
    year = int(input_day[:4])
    month = int(input_day[4:6])
    day = int(input_day[6:])
    if month == 0 or month > 12 or day == 0 or day > 31 or year < 1:
        print(f'#{t} -1')
    elif month == 2 and day > 28:
        print(f'#{t} -1')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 31:
            print(f'#{t} -1')
        else:
            print(f'#{t} {input_day[:4]}/{input_day[4:6]}/{input_day[6:]}')
    else:
        print(f'#{t} {input_day[:4]}/{input_day[4:6]}/{input_day[6:]}')
