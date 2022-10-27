# prog_12901 이상한_문자_만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 2월은 29일까지
def solution(a, b):
    end_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 모든 달을 일수로 변경
    for days in range(1, a):
        b += end_of_month[days]
    print(b)
    return day_of_week[b % 7]


print(solution(5, 24))
