t = int(input())

for tc in range(1, t + 1):

    x, y = map(int, input().split())

    print(f'#{tc} {x // y} {x % y}')
