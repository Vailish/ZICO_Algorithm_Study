a, b = map(int, input().strip().split(' '))

while b:
    print('*' * a)
    b -= 1

for _ in range(b):
    print('*' * a)