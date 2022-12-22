# 생성 가능한 수 집합에 저장
def chk(word):
    for i in range(0, n, m):
        number = int(word[i : i+m], 16)
        numbers.add(number)


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    m = n // 4
    password = input()
    numbers = set()
    chk(password)
    for _ in range(m-1):
        password = password[-1] + password[:-1]
        chk(password)

    result = sorted(numbers, reverse=True)
    print(f'#{t} {result[k-1]}')
