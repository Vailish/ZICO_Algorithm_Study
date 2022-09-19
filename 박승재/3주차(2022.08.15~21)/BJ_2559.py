import sys

N, K = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
num_sum = sum(num_list[:K])

highest_sum = num_sum
for i in range(len(num_list)-K):
    num_sum = num_sum - num_list[i] + num_list[i+K]
    if highest_sum < num_sum:
        highest_sum = num_sum

print(highest_sum)

