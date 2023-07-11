t = int(input())
for tc in range(t):
    n = int(input())
    total_str = ""
    for _ in range(n):
        alpa, num = input().split()
        total_str += alpa * int(num)

    print(f"#{tc + 1}")
    for i in range(0, len(total_str), 10):
        print(total_str[i : i + 10])
