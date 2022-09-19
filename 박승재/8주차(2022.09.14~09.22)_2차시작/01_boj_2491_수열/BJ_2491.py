# import sys
#
# input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
up = 1
down = 1
up_down_list = []
for i in range(n - 1):
    if nums[i] < nums[i + 1]:
        up += 1
        if down > 1:
            up_down_list.append(down)
            down = 1
    elif nums[i] > nums[i + 1]:
        down += 1
        if up > 1 :
            up_down_list.append(up)
            up = 1
    else:
        up += 1
        down += 1
up_down_list.append(max(up, down))
print(max(up_down_list))
