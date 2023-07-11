import sys
sys.stdin = open("input.txt")

N = int(input())
result = []
increase_length = 1
decrease_length = 1
increase = 0
decrease = 0
nums = list(map(int,input().split()))
for idx in range(N-1):
    if nums[idx] > nums[idx+1]:
        decrease_length += 1
        result.append(increase_length)
        increase_length = 1
    elif nums[idx] < nums[idx+1]:
        increase_length += 1
        result.append(decrease_length)
        decrease_length = 1
    else:
        decrease_length += 1
        increase_length += 1

result.append(increase_length)
result.append(decrease_length)

print(max(result))

print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
