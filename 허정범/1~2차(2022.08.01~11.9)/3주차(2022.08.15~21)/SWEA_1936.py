a, b = map(int, input().split())

if a == 1:
    print("B") if b is 2 else print("A")
elif a == 2:
    print("A") if b is 1 else print("B")
elif a == 3:
    print("B") if b is 1 else print("A")
