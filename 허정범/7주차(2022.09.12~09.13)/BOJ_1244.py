length = int(input())
sw_state = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    gender, num = map(int, input().split())
    # 남자
    if gender == 1:
        for i in range(length):
            if (i + 1) % num == 0:
                sw_state[i] = int(not sw_state[i])
    # 여자
    else:
        sw_state[num - 1] = int(not sw_state[num - 1])
        cnt = 1
        while True:
            l, r = num - 1 - cnt, num - 1 + cnt
            if l < 0 or r >= length or sw_state[l] != sw_state[r]:
                break
            sw_state[l] = int(not sw_state[l])
            sw_state[r] = sw_state[l]
            cnt += 1


for idx in range(0, length, 10):
    print(*sw_state[idx : idx + 10])
