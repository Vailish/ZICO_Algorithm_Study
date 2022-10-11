t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    result = "Possible"

    for i in range(n):
        bbang = (arrive[i] // m) * k
        if bbang < i + 1:
            result = "Impossible"
            break

    print(f"#{tc + 1} {result}")
