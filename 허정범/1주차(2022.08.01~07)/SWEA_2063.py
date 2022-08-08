t_num = int(input())
numbers_list = list(map(int, input().split()))
numbers_list.sort()
print(f"{numbers_list[(t_num-1)//2]}")
