#2050. 알파벳을 숫자로 변환 D1
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE&problemTitle=2050&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# ASCII ord() , chr()

Words = input()
for word in Words:
    print(ord(word)-64, end=" ")