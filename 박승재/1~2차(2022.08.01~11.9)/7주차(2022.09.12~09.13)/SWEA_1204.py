def sol():
    case = int(input())
    num_list = list(map(int, input().split()))
    chk = sorted(list(set(num_list)))
    cnt = 0
    for num in chk:
        num_cnt = num_list.count(num)
        if cnt <= num_cnt:
            cnt = num_cnt
            result = num
    print(result)
    return


for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()
