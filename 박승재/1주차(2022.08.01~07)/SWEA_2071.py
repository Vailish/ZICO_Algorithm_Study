T = int(input())
for case in range(T):
    print(f'#{case+1} {round(sum(list(map(int, input().split())))/10)}')
