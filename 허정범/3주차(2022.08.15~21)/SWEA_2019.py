n = int(input())
list_a = [1]
for i in range(n):
    list_a.append(list_a[i] * 2)
print(*list_a)
