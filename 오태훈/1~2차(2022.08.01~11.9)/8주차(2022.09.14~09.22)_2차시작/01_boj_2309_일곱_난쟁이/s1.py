# 2309. 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

arr = [int(input()) for _ in range(9)]

sum_n = sum(arr)

num = sum_n - 100

for i in arr:
    n = num - i
    if n in arr and n != i:
        num1 = i
        num2 = n
del arr[arr.index(num1)]
del arr[arr.index(num2)]

print(*sorted(arr), sep='\n')
