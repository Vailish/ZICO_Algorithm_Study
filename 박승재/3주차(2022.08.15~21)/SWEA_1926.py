n = int(input())

num_369 = ['3', '6', '9']
for i in range(1, n+1):
    count = 0
    for st in str(i):
        if st in num_369:
            count += 1
    if count == 0:
        print(i, end=' ')
    else:
        print('-'*count, end=' ')
