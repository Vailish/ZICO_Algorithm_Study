# 2072. 홀수만 더하기

T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    sum_value = 0
    for number in numbers:
        if number % 2 != 0:
            sum_value += number
        else:
            pass
    print(f'#{t} {sum_value}')
