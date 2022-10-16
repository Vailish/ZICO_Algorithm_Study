# 1주차
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total_price = 0
    for cnt in range(count):
        total_price += price * (cnt+1)
    return total_price - money if total_price > money else 0