
T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    word = input()
    result = 1
    # level
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            result = 0
            break
    print(result)
