def sol():
    N, M = map(int, input().split())
    if N < M:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
    result = 0
    for i in range(len(B)-len(A)+1):
        chk_sum = 0
        for j in range(len(A)):
            chk_sum += A[j] * B[i+j]
        if result < chk_sum:
            result = chk_sum
    return print(result)


for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()


