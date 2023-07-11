N = int(input())
result = 0
while True:
    result += N % 10
    N = N // 10
    if N == 0:
        print(result)
        break

print(sum(list(map(int, list(input())))))
