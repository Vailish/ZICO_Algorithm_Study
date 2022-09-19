import sys
sys.stdin = open("input.txt")

N = int(input())
result = 1
increase = 0
decrease = 0
is_down = True
is_up = True
nums = list(map(int,input().split()))
for idx in range(N-1):
    if is_up and nums[idx] > nums[idx+1]:
        if result < idx - increase:
            result = idx - increase
        increase = idx + 1
        decrease = idx
        is_down = True
        is_up = False
    elif is_down and nums[idx] < nums[idx+1]:
        if result < idx - decrease:
            result = idx - decrease
        decrease = idx + 1
        increase = idx
        is_up = True
        is_down = False

print(max(result,N-decrease,N-increase))

print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
