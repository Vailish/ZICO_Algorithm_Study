t_num = int(input())
for idx in range(t_num):
    numbers_list = list(map(int, input().split()))
    print(f"#{idx+1} {max(numbers_list)}")
