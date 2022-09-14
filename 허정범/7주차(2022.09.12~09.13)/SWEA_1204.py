t = int(input())
for _ in range(t):
    tc = int(input())
    input_num = list(map(int, input().split()))
    count_dict = {}

    for num in input_num:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sort_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print(f"#{tc} {sort_dict[0][0]}")
