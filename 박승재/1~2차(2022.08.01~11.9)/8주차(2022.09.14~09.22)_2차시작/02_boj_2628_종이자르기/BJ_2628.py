def chk_length(num_list):
    answer = 0
    start = 0
    for number in num_list:
        length = number - start
        if answer < length:
            answer = length
        start = number
    return answer


row, col = map(int, input().split())
row_list = [row]
col_list = [col]
for _ in range(int(input())):
    direction, num = map(int, input().split())
    if direction == 0:
        col_list.append(num)
    elif direction == 1:
        row_list.append(num)
print(chk_length(sorted(row_list)) * chk_length(sorted(col_list)))
