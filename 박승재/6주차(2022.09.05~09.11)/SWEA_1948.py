def sol():
    m1, d1, m2, d2 = map(int, input().split())
    result = d2 - d1 + 1
    while m1 != m2:
        result += month[m1]
        m1 += 1
    print(result)
    return


month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()