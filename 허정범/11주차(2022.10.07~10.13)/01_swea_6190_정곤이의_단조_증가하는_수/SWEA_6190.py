t = int(input())
for tc in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    max_v = -1
    for i in range(n - 1):
        for k in range(i + 1, n):
            num = nums[i] * nums[k]
            if max_v >= num:
                continue
            danjo = []
            while num:
                danjo.append(num % 10)
                num = num // 10
            for j in range(len(danjo) - 1):
                if danjo[j] < danjo[j + 1]:
                    break
            else:
                max_v = nums[i] * nums[k]

    print(f"#{tc + 1} {max_v}")