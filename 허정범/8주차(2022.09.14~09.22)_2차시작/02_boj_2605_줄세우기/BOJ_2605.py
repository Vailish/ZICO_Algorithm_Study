n = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(n):
    result.insert(arr[i], i + 1)
print(*result[::-1])