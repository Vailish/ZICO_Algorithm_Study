def sol():
    answer = 0
    v = 0
    for _ in range(int(input())):
        c = list(map(int, input().split()))
        if c[0] == 1:
            v += c[1]
        elif c[0] == 2:
            if v - c[1] < 0:
                v = 0
            else:
                v -= c[1]
        answer += v

    print(answer)
    return


for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()