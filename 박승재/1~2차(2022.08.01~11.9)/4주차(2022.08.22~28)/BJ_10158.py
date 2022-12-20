
w, h = map(int, input().split())

x, y = map(int, input().split())

hour = int(input())

x += hour
y += hour

if (x // w) % 2:
    x = w - x % w
else:
    x = x % w

if (y // h) % 2:
    y = h - y % h
else:
    y = y % h

print(x, y)
