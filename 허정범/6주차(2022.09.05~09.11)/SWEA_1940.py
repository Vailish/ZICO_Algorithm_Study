t = int(input())
for tc in range(t):
    n = int(input())
    total_length = 0
    v = 0
    for _ in range(n):
        input_num = input()
        if input_num == "0":
            total_length += v
            continue
        t, dv = map(int, input_num.split())
        if t == 1:
            v += dv
        else:
            v -= dv
            if v < 0:
                v = 0
        total_length += v

    print(f"#{tc + 1} {total_length}")
