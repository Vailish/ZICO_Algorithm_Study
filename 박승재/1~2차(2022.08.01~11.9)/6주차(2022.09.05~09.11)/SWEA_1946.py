def sol():
    t = int(input())
    a = ''
    for x in range(1, t + 1):
        eng, num = input().split()
        res = eng * int(num)
        a += res
    for y in range(0, len(a) + 1, 10):
        print(a[0:10])
        a = a[10:]
    return


for test_case in range(1, int(input())+1):
    print(f'#{test_case}')
    sol()
