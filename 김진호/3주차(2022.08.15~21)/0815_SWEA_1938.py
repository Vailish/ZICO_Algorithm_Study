##################################################
# 1. 일반적인 계산기

a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)

##################################################
# 2. eval 사용 (swea 사용불가)

a, b = input().split()
cals = ['+', '-', '*', '//']

for cal in cals:
    print(eval(a + cal + b))

##################################################
