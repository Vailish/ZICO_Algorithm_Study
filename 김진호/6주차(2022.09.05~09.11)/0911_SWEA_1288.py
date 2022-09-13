for test_case in range(1,int(input())+1):
    N = int(input())
    num_set = set()
    i = 1
    while len(num_set) != 10:
        words = str(N * i)
        for word in words:
            num_set.add(word)
        i += 1
    print(f'#{test_case} {int(words)}')