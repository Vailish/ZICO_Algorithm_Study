def solution(price, money, count):
    money -= sum(range(1, count + 1)) * price
    if money > 0:
        money = 0
    return -money
