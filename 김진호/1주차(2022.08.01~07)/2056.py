mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월에 대한 일수 리스트
T = int(input())
for test_case in range(1, T + 1):
    ymd = input()
    year = int(ymd[0:4])  # 연도 추출
    month = int(ymd[4:6])  # 월 추출
    day = int(ymd[6:8])  # 일자 추출

    if year != 0 and 0 < month <= 12:  # 연도와 월이 정상적인지 검증
        if mon_day[month - 1] >= day > 0:  # 일자가 월에 맞게 정상적인지 검증
            print(f'#{test_case} {ymd[0:4]}/{ymd[4:6]}/{ymd[6:8]}')  # 정상이므로 연년도 출력
        else:
            print(f'#{test_case} -1')
    else:
        print(f'#{test_case} -1')

        # 모든 else는 정상적인 연년도가 아니므로 -1 출력
