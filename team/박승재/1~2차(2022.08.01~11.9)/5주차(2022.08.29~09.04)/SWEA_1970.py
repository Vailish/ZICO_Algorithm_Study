def sol():
    N = int(input())
    for money in money_list:
        print(N//money, end=' ')
        N %= money
    print()


money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, int(input())+1):
    print(f'#{test_case}')
    sol()
    