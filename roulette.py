from random import *
import random

############
# Roulette #
############

순서 = ['( ´ิ(ꈊ) ´ิ) 1등!', 2, 3, 4, 5, 6]

제목 = ['Magnetic', '행렬찾기', '작업순서', '숫자배열회전', '선택', '선택']

뽑기 = ['( σ̴̶̷̤ .̫ σ̴̶̷̤ )♡ 당첨 ৻( •̀ ᗜ •́ ৻)', '꽝', '꽝', '꽝', '꽝', '꽝']

problems = random.sample([0, 1, 2, 3, 4, 5], 6)
people = random.sample(['김성준', '김진호', '박승재', '오태훈', '이가은', '허정범'], 6)

### 함수 ###
def rnd():
    people = random.sample(['김성준', '김진호', '박승재', '오태훈', '이가은', '허정범'], 6)
    problems = random.sample([0, 1, 2, 3, 4, 5], 6)


### 로직 ###
while True:
    print(
        '''##################################################
1. 순서 정하기
2. 뽑기
##################################################'''
    )
    print('모드를 선택하세요. :', end=' ')
    answer = int(input())
    if answer == 1:
        pass
    else:
        print('다시 눌러주세요')


### 출력단 ###
print('#' * 50)
for i in range(6):
    print(f'{people[i]} : {뽑기[problems[i]]}')
print('#' * 50)
