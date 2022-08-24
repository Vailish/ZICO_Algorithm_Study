
T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    words = input()

    for i in range(1, 11):
        if words[:11] == words[i:11+i]:
            print(i)
            break