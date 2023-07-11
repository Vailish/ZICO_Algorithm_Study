# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq

# 저장하여 한번에 출력

for test_case in range(1, int(input())+1):
    num = int(input())
    result = []
    for prime in [2, 3, 5, 7, 11]:
        cnt = 0
        while num % prime == 0:
            num = num // prime
            cnt += 1
        result.append(cnt)

    print(f'#{test_case} ', *result)

# 저장없이 계속 출력

for test_case in range(1, int(input())+1):
    num = int(input())
    print(f'#{test_case}', end=' ')
    for prime in [2, 3, 5, 7, 11]:
        cnt = 0
        while num % prime == 0:
            num = num // prime
            cnt += 1
        print(cnt, end=' ')
    print()

# 저장하여 한번에 출력 2

for test_case in range(1, int(input())+1):
    num = int(input())
    result = ''
    for prime in [2, 3, 5, 7, 11]:
        cnt = 0
        while num % prime == 0:
            num = num // prime
            cnt += 1
        result += f'{cnt} '
    print(f'#{test_case} {result}')
