# 2056. 연월일 달력

# T = int(input())

# for t in range(1, T + 1):
#     number = input()
#     month_31 = ['01', '03', '05', '07', '08', '10', '12']
#     month_30 = ['04', '06', '09', '11']
#     month_28 = ['02']
#     if number[4:6] in month_31 and 1 <= int(number[6:8]) <= 31:
#         date = f'{number[0:4]}/{number[4:6]}/{number[6:8]}'
#     elif number[4:6] in month_30 and 1 <= int(number[6:8]) <= 30:
#         date = f'{number[0:4]}/{number[4:6]}/{number[6:8]}'
#     elif number[4:6] in month_28 and 1 <= int(number[6:8]) <= 28:
#         date = f'{number[0:4]}/{number[4:6]}/{number[6:8]}'
#     else:
#         date = -1
#     print(f'#{t} {date}')

import datetime

T = int(input())

for testcase in range(1, T + 1):
    number = input()
    str_date = f'{number[:4]}-{number[4:6]}-{number[6:]}'  # YYYY-MM-DD 형식으로 변환
    try:  # 날짜 형식에 맞는지 체크
        datetime.datetime.strptime(str_date, '%Y-%m-%d')
    except ValueError:  # ValueError발생 시 -1 출력
        print(f'#{testcase} -1')
        continue
    date = str_date.replace('-', '/')
    print(f'#{testcase} {date}')  # -를 / 로 바꾼 후 출력
