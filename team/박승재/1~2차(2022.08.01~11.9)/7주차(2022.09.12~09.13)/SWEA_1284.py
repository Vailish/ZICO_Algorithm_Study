def sol():
    p, q, r, s, w = map(int, input().split())
    answer1 = p * w
    answer2 = q
    if w > r:
        answer2 += s * (w - r)
    if answer1 < answer2:
        print(answer1)
        return
    print(answer2)
    return


for test_case in range(1, int(input())+1):
    print(f'#{test_case}', end=' ')
    sol()