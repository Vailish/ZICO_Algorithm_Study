T = int(input())
for t in range(1, 1 + T):
    list_number = list(map(int, input().split()))
    answer = 0
    for number in list_number:
        if number % 2:
            answer += number
    print(f'#{t} {answer}')

T = int(input())
for t in range(1, 1 + T):
    number_list = [number for number in list(map(int, input().split())) if 1 % 2]
    print(f'#{t} {sum(number_list)}')
