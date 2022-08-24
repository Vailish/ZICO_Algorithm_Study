n, k = map(int, input().split())
nums_list = list(map(int, input().split()))

# max_sum = sum(nums_list[0:k])
# row_sum = sum(nums_list[0:k])

# sum메서드 안쓰고 풀기
max_sum = 0
row_sum = 0
for idx in range(k):
    max_sum += nums_list[idx]
    row_sum += nums_list[idx]

for i in range(n - k):
    row_sum += nums_list[i + k] - nums_list[i]
    if max_sum < row_sum:
        max_sum = row_sum
print(max_sum)
