def sol():
    N = int(input())

    num_list = sorted(list(map(int, input().split())))

    print(*num_list)


for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()
