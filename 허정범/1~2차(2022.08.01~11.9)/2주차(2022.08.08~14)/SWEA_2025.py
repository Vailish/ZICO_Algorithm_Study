# num = int(input())
# sum_num = 0
# for i in range(num):
#     sum_num += i + 1
# print(sum_num)

numbers = [i + 1 for i in range(int(input()))]
print(sum(numbers))
