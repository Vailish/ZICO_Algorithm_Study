# 1936. 1대1 가위바위보

b = input().split()

if b[0] == '1':
    if b[1] == '2':
        print('B')
    else:
        print('A')
elif b[0] == '2':
    if b[1] == '3':
        print('B')
    else:
        print('A')
elif b[0] == '3':
    if b[1] == '1':
        print('B')
    else:
        print('A')
