# 2068. 최대수 구하기
T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))

    max_number = max(numbers)

    print(f'#{t} {max_number}')
