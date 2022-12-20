t = int(input())
for tc in range(t):
    div_numbers = [2, 3, 5, 7, 11]
    output_list = []
    n = int(input())

    for div_num in div_numbers:
        cnt = 0
        while True:
            if not (n % div_num):
                n = n // div_num
                cnt += 1
            else:
                break
        output_list.append(cnt)
    print(f"#{tc+1}", *output_list)
