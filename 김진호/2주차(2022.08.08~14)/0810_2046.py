# 기본 출력
print('#'*int(input()))

# for문
for _ in range(int(input())):
    print('#', end='')

# sys.stdout.write로 개행제거
import sys
for _ in range(int(input())):
    sys.stdout.write('#')


'''----------------------------------------------------------------
print               = 입력 마지막에 줄바꿈 O , 메모리 적다 , 출력이 느림
sys.stdout.write    = 입력 마지막에 줄바꿈 X , 메모리 크다 , 출력이 빠름
-----------------------------------------------------------------'''


# 시간, 메모리 측정
import sys
import time

Str = ""

start_time_1 = time.time()

for _ in range(1000000):
    print(Str)

end_time_1 = time.time()

start_time_2 = time.time()

for _ in range(1000000):
    sys.stdout.write(Str)

end_time_2 = time.time()

print()
print("print 소요시간 :", end_time_1-start_time_1)
print("sys.stdout.write 소요시간 :", end_time_2-start_time_2)

'''----------------------------------------------------------------
print 소요시간 : 약 1.84초
sys.stdout.write 소요시간 : 약 0.28초

출력함수 호출이 많을수록 시간 증가량이 크다
(그런데 알고리즘에서 A까지는 이거 문제로 시간초과는 잘 안생길듯)
-----------------------------------------------------------------'''
