t = int(input())

for tc in range(t):
    input_date = input()
    y = input_date[:4]
    m = input_date[4:6]
    d = input_date[6:]
    able_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(y) < 0:
        print(f"#{tc+1} -1")
    elif not (1 <= int(m) <= 12):
        print(f"#{tc+1} -1")
    elif 0 < int(d) <= able_day[int(m) - 1]:
        print(f"#{tc+1} {y}/{m}/{d}")
    else:
        print(f"#{tc+1} -1")
