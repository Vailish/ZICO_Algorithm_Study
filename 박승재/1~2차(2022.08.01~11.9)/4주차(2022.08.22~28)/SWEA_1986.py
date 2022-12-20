T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}', end=' ')

    if N % 2:
        print(N // 2 + 1)
    else:
        print(-N // 2)

