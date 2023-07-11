n=int(input())
print(*[m for m in range(1,n+1)if n%m==0])