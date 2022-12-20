t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print(f"#{tc + 1} {sum(scores[:k])}")