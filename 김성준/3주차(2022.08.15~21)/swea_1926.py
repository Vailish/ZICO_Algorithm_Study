# 1926. 간단한 369게임 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq

N = int(input())

arr = list(range(1, 1 + N))

for num in (range(1, 1 + N)):
    cnt = 0
    for n in str(num):
        if n in '369':
            cnt += 1
    if cnt == 1:
        num = '-'
    elif cnt == 2:
        num = '--'
    elif cnt == 3:
        num = '---'
    else:
        num = str(num)
    print(num, end=' ')

'''
카운트를 셋으면 그냥 그걸 곱하면 되잖음!!
N = int(input())
 
li = ['3', '6', '9']
 
for i in range(1, N+1):
    cnt = 0
    for j in str(i):
        if j in li:
            cnt += 1
    if cnt > 0:
        i = '-' * cnt
     
    print(i, end = ' ')
'''