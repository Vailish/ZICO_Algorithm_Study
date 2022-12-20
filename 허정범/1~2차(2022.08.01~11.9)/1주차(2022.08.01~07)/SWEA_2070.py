t_num = int(input())
for idx in range(t_num):
    number1, number2 = map(int, input().split())
    if number1 > number2:
        print(f"#{idx+1} >")
    elif number1 < number2:
        print(f"#{idx+1} <")
    else:
        print(f"#{idx+1} =")
