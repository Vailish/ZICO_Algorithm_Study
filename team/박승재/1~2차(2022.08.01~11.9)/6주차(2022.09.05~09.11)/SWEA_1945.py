def sol():
    count = [0] * 5
    N = int(input())
    for num in range(5):
        while True:
            if N % alph[num] == 0:
                N = N // alph[num]
                count[num] += 1
            else:
                break
    print(*count)
    return


alph = [2, 3, 5, 7, 11]
for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()
