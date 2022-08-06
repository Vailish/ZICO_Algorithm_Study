T = int(input())

for test_case in range(1, T + 1):
    list_num = list(map(int, input().split()))
    print(f'#{test_case} {max(list_num)}')
