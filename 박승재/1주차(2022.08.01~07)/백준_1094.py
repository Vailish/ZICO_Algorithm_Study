# x = int(input())
# count = 0
# n = 64
# while True:
#     if x == n or x == n / 2:
#         count += 1
#         break
#     elif x > n / 2:
#         x -= n / 2
#         n = n / 2
#         count += 1
#     else:
#         n = n / 2
# print(count)

# 합해진 막대기의 크기를 알고 싶을때

x = int(input())
count = []
n = 64
while True:
    if x == n or x == n / 2:
        n = n / 2
        count.append(n)
        break
    elif x > n / 2:
        x -= n / 2
        n = n / 2
        count.append(n)
    else:
        n = n / 2
print(count)
print(len(count))
