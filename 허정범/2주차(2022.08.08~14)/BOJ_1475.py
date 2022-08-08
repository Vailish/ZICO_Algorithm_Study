str = input()
cnt = [0] * 10
for num in str:
    cnt[int(num)] += 1
max_num = (cnt[6] + cnt[9]) // 2 + (cnt[6] + cnt[9]) % 2
for i in range(10):
    if i == 6 or i == 9:
        continue
    if max_num < cnt[i]:
        max_num = cnt[i]
print(max_num)
