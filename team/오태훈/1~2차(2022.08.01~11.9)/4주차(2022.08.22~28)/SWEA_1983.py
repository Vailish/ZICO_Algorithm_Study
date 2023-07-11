# 1983. 조교의 성적 매기기

grade = {
    0: 'A+',
    1: 'A0',
    2: 'A-',
    3: 'B+',
    4: 'B0',
    5: 'B-',
    6: 'C+',
    7: 'C0',
    8: 'C-',
    9: 'D0',
}
for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr = list(map(lambda x: x[0] * 0.35 + x[1] * 0.45 + x[2] * 0.2, arr))
    target = arr[k - 1]
    idx = sorted(arr, reverse=True).index(target)
    print(f'#{t}', grade[idx // (n // 10)])
