T = int(input())
for case in range(T):
    number_list = list(map(int, input().split()))
    highest_number = 0
    for number in number_list:
        if highest_number < number:
            highest_number = number
    print(f'#{case + 1} {highest_number}')
