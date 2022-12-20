n = int(input())
num_list = [str(i) for i in range(1, n + 1)]
for i in range(n):
    num_list[i] = num_list[i].replace("3", "-")
    num_list[i] = num_list[i].replace("6", "-")
    num_list[i] = num_list[i].replace("9", "-")
    if num_list[i].count("-") == 1:
        num_list[i] = "-"

str_nums = " ".join(num_list)
print(str_nums)
