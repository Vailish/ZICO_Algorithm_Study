T = int(input())
for test_case in range(T):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{test_case + 1} >')
    elif a < b:
        print(f'#{test_case + 1} <')
    else:
        print(f'#{test_case + 1} =')
