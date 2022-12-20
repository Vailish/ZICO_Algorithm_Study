def sol():
    N = int(input())
    chk = set()
    answer = 0
    while len(chk) < 10:
        answer += 1
        n = N * answer
        while n > 0:
            chk.add(n%10)
            n = n // 10
    print(N * answer)
    return


for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()