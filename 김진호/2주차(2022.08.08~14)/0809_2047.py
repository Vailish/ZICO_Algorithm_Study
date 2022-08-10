# 기본 출력
print(input().upper())

# for문
for s in input():
    print(s.upper(), end='')

# 소문자 검증 & 아스키코드 값으로 대문자로 출력
for s in input():
    if s.islower() == 1:
        print(chr(ord(s)-32), end='')
        continue
    print(s, end='')