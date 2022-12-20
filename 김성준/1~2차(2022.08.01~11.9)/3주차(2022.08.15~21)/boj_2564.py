# 경비원 실버1
# https://www.acmicpc.net/problem/2564

h, w = list(map(int,input().split()))  # 블록의 가로 세로
num_store = int(input())  # 상점 개수
store = [list(map(int, input().split())) for _ in range(num_store)]
dong_d, dong_l = list(map(int, input().split()))
result = 0  # 각 최단 거리의 합

# dong과 같은 line
if dong_d == 1 or dong_d == 2:
    line = w  # dong과 수평인 라인
    line_v = h  # dong과 수직인 라인
else:
    line = h
    line_v = w

# 검사
for store_d, store_l in store:
    # dong과 같은 line 일 때
    if dong_d == store_d:
        result += abs(dong_l - store_l)
    
    # dong과 평행한 line 일 때
    elif store_d == line:
        if  dong_l + store_l + line_v <= line * 2 - dong_l - store_l + line_v:
            result += dong_l + store_l + line_v
        else:
            result += line * 2 - dong_l - store_l + line_v
    
    # dong과 인접한 line 일 때
    else:
        # if dong_l + line_v - store_l <=  line + line_v - dong_l - store_l:
        if dong_l + line_v - store_l <=  line + line_v - dong_l - store_l:
            result += dong_l + line_v - store_l
        else:
            result += line + line_v - dong_l - store_l
print(result)

# 이동하면서 count 해서 구해주기