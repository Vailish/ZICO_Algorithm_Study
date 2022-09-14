t = int(input())
for tc in range(t):
    n = int(input())
    num_set = set()
    i = 0
    while len(num_set) != 10:
        i += 1
        num_list = list(map(int, str(n * i)))
        num_set.update(num_list)

    print(f"#{tc + 1} {i * n}")
