# 1945. 간단한 소인수분해
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq
for test_case in range(1, int(input()) + 1):
    number = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    # 2로 나눠지면 나누기
    while number % 2 == 0:
        number /= 2
        a += 1
    # 3으로 나눠지면 나누기
    while number % 3 == 0:
        number /= 3
        b += 1
    # 5로 나눠지면 나누기
    while number % 5 == 0:
        number /= 5
        c += 1
    # 7로 나눠지면 나누기
    while number % 7 == 0:
        number /= 7
        d += 1
    # 11로 나눠지면 나누기
    while number % 11 == 0:
        number /= 11
        e += 1

    print(f'#{test_case}', a, b, c, d, e, sep=' ')
