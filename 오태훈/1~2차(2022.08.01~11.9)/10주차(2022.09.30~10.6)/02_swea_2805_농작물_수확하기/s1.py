for t in range(1, int(input()) + 1):
    n = int(input())

    farm = [list(map(int, input())) for _ in range(n)]
    cnt, result, middle = 0, 0, n // 2
    turn = False
    for line in farm:
        result += sum(line[middle - cnt : middle + cnt + 1])
        if cnt == middle:
            turn = True
        if turn:
            cnt -= 1
        else:
            cnt += 1

    print(f'#{t} {result}')
