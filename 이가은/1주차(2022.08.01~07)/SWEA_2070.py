# 큰 놈, 작은 놈, 같은 놈

t = int(input())

for test_case in range(1, t + 1):
    x, y = map(int, input().split())
    if x < y:
        print(f'#{test_case} <')

    elif x > y:
        print(f'#{test_case} >')

    elif x == y:
        print(f'#{test_case} =')
