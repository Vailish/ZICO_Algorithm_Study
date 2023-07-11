# 1244. 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
switch_n = int(input())
switch_status = list(map(int, input().split()))

student_n = int(input())


for _ in range(student_n):
    s, value = map(int, input().split())
    if s == 1:
        # 남학생일 경우 연산
        for i in range((value - 1), switch_n, value):
            switch_status[i] = int(not (switch_status[i]))

    else:
        # 여학생일 경우 연산
        value -= 1
        switch_status[value] = int(not switch_status[value])
        j = 1
        while True:
            if value - j < 0 or value + j >= switch_n:
                break
            elif switch_status[value - j] == switch_status[value + j]:
                switch_status[value - j] = int(not switch_status[value - j])
                switch_status[value + j] = int(not switch_status[value + j])
                j += 1
            else:
                break
count = 0
for arr_value in switch_status:
    if count == 20:
        count = 0
        print()
    print(arr_value, end=' ')
    count += 1
