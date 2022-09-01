t = int(input())

for tc in range(t):
    str_line = input()
    cnt = 0
    for i in range(1, len(str_line)):
        if str_line[0] == str_line[i]:
            if str_line[:i] == str_line[i : i + i]:
                cnt = i
                break
    print(f"#{tc + 1} {cnt}")
