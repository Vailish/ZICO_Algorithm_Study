t = int(input())
for tc in range(t):
    num_list = list(map(int, input().split()))
    num_list.sort()
    print(f"#{tc + 1} {round(sum(num_list[1:9]) / 8)}")