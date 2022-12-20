def chk(line):
    if line.count(1) < k:
        return 0
    sum_1 = 0
    for i in line:
        if i == 1:
            sum_1 += 1
        elif i == 0:
            sum_is_k(sum_1)
            sum_1 = 0
    sum_is_k(sum_1)


def sum_is_k(s):
    global result
    if s == k:
        result += 1


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for w in arr:
        chk(w)
    for e in list(zip(*arr)):
        chk(e)

    print(f'#{t} {result}')
