def sol():
    for tc in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        test_result = list(map(int, input().split()))
        test_result.sort(reverse=True)
        print('#{} {}'.format(tc, sum(test_result[:k])))


sol()