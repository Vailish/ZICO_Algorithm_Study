def sol():
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for case in range(1, 1 + int(input())):
        price = int(input())
        print(f'#{case}')

        for cash in money:
            cnt = 0
            while True:
                if price >= cash:
                    price -= cash
                    cnt += 1
                else:
                    print(cnt, end=' ')
                    break
        print()


sol()
