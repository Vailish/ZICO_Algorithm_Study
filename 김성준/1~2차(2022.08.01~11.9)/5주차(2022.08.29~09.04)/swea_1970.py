# 1970. 쉬운 거스름돈 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq

# for 문으로 돈 리스트를 돌리면서 그 개수를 출력하자
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
                if cnt == 0:
                    print('0', end=' ')
                else:
                    print(str(cnt), end=' ')
                break
    print()