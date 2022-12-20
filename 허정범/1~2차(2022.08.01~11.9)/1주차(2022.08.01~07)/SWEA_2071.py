t_num = int(input())
for idx in range(t_num):
    # numbers_list = [number for number in map(int, input().split())]
    numbers_list = list(map(int, input().split()))
    print(f"#{idx+1} {round(sum(numbers_list)/len(numbers_list))}")
