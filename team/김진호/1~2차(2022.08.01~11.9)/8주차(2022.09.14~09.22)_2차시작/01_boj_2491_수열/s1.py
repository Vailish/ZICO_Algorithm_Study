import sys
sys.stdin = open("input.txt")

N = int(input())
result = 0
increase_length = 1
decrease_length = 1
nums = list(map(int,input().split()))
for idx in range(N-1):
    if nums[idx] > nums[idx+1]:
        decrease_length += 1
        if result < increase_length:
            result = increase_length
        increase_length = 1
    elif nums[idx] < nums[idx+1]:
        increase_length += 1
        if result < decrease_length:
            result = decrease_length
        decrease_length = 1
    else:
        decrease_length += 1
        increase_length += 1

print(max(result,increase_length,decrease_length))


print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
