# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

for _ in range(1, 1 + int(input())):
    case = int(input())
    arr = list(map(int, input().split()))
    mode = [0, 0]  # 최빈값 = [value, times]
    for num in sorted(list(set(arr))):  # 정렬안하고 set만 사용시 동일 값 중 최대값이 아닐 수 있음
        if arr.count(num) >= mode[1]:
            mode[0] = num
            mode[1] = arr.count(num)
    print(f'#{case} {mode[0]}')
