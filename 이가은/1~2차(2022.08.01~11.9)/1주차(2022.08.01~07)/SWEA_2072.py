t = int(input())

for test_case in range(1, t + 1):
    numbers = map(int, input().split())
    sum = 0  # 받은 입력값과 합을 테스트 케이스마다 초기화 시켜줘야하기 때문에 for문 안쪽에 변수 선언.
    for number in numbers:
        if number % 2 == 1:
            sum += number

    print(f'#{test_case} {sum}')
