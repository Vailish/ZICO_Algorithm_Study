a, b = map(int, input().split())
# 1 가위 / 2 바위 / 3 보

if a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2:
    print('A')
else:
    print('B')