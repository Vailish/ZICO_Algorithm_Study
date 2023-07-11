import sys
sys.stdin = open("input.txt")

K = int(input())
nums = []
max_num, max_idx = 0, 0
for idx in range(6):
    pos, dis = map(int,input().split())
    nums.append(dis)
    if max_num < dis:
        max_num = dis
        max_idx = idx
if nums[max_idx-1] < nums[(max_idx+1)%6]:
    result = nums[max_idx] * nums[(max_idx+1)%6] - nums[(max_idx+3)%6] * nums[(max_idx+4)%6]
else:
    result = nums[max_idx] * nums[(max_idx - 1)] - nums[(max_idx+2)%6] * nums[(max_idx+3)%6]

print(result*K)

print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
