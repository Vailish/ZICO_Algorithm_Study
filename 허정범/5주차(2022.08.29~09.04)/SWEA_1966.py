t = int(input())
for tc in range(t):
    n = int(input())
    list_a = sorted(list(map(int, input().split())))
    print(f"#{tc + 1}", *list_a)
