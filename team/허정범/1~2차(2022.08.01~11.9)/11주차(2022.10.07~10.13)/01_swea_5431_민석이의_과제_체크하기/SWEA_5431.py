t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    people = set(range(1, n + 1))
    person = set(map(int, input().split()))
    print(f"#{tc + 1}", *sorted(people-person))