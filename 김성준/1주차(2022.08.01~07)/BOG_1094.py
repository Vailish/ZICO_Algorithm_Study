#막대기 1094번 실버5
#https://www.acmicpc.net/problem/1094
x=int(input())
sticks = [64] # 64 32 16 8 4 2 1
# 64 => 32 32
# >        16 16
while sum(sticks) != x and x != 64:
    if sum(sticks) > x:
        half_sticks = min(sticks)/2
        sticks.remove(min(sticks))
        sticks.append(half_sticks)
        if sum(sticks) >= x:
            # half_sticks = min(sticks)/2
            # sticks.remove(min(sticks))
            # sticks.append(half_sticks)
            sticks.remove(max(sticks))
            sticks.append(half_sticks)
    else:
        break
print(len(sticks))