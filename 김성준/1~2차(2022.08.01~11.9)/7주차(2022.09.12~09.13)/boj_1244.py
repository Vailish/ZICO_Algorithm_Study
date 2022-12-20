# 1244 스위치 켜고 끄기 실버4
# https://www.acmicpc.net/problem/1244

def chk(data):
    if swich[data] == 0:
        swich[data] = 1
    else:
        swich[data] = 0


num = int(input())  # 스위치 개수
swich = list(map(int, input().split()))
students = int(input())  # 학생 수
for _ in range(students):
    index, value = map(int, input().split())  # index, value = 성별, 스위치 값
    if index == 1:  # 남학생일 경우  value의 배수
        k = 1
        while value * k <= num:  # 정말 감사합니다
            chk(value * k - 1)
            k += 1
    else:  # 여학생일 경우 left value-2 [value -1] value right
        left = value - 2
        right = value
        chk(value - 1)
        while left >= 0 and right <= num - 1:  # 예외처리
            if swich[left] == swich[right]:
                chk(left)
                chk(right)
                left -= 1
                right += 1
            else:
                break
timer = 0
for result in swich:
    timer += 1
    print(result, end=' ')
    if timer >= 20:
        print()
        timer = 0


# if num <= 20:
#     numb = 1
# elif 20 < num <= 40:
#     numb = 2
# elif 40 <= num < 60:
#     numb = 3
# elif 60 <= num < 80:
#     numb = 4
# else:
#     numb = 5
#
# for _ in range(numb):
#     swich += list(map(int, input().split()))
