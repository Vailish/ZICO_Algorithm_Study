from random import *
import random

############
# Roulette #
############

순서 = ['( ´ิ(ꈊ) ´ิ) 1등!', 2, 3, 4, 5, 6]

제목 = [
    'Magnetic',
    '행렬찾기',
    '작업순서',
    '숫자배열회전',
    '선택',
    '선택'
    ]

뽑기 = [
    '( σ̴̶̷̤ .̫ σ̴̶̷̤ )♡ 당첨 ৻( •̀ ᗜ •́ ৻)',
    '꽝',
    '꽝',
    '꽝',
    '꽝',
    '꽝'
]

problems = random.sample([0, 1, 2, 3, 4, 5], 6)
people = random.sample(['김성준', '김진호', '박승재', '오태훈', '이가은', '허정범'], 6)
for i in range(6):
    print()
    print(f'# {people[i]} : {순서[problems[i]]}')
    