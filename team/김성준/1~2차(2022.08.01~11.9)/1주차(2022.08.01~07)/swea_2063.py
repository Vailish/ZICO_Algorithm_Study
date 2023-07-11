#2063.중간값 찾기 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=2063&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

N = int(input())
M = list(map(int,input().split()))
M.sort()
print(M[N//2])
