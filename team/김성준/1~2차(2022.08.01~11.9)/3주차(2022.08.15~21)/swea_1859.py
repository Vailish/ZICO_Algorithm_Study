# 1859. 백만 장자 프로젝트 D2
# https://swexpertacademy.com/main/code/problem/problemSubmitDetail.do

for case in range(1, 1 + int(input())):
    days = int(input())  # 총 기간
    info = list(map(int, input().split()))  # 각 날 별 매매가

    # 최대값 찾고, 최대값 기준으로 앞부분 처리 후 삭제, 반복(마지막 자리가 최대값이 될때까지)
    # 최대값 = 최대값 * 개수 - 해당지점까지 총합
    revenue = 0  # 수익
    max_price = max(info)
    while True:
        max_price = max(info)
        if max_price == info[-1]:
            revenue += max_price * len(info) - sum(info)
            break
        elif max_price == info[0]:  # 최고가가 제일 앞에(역리스트에서는 제일 뒤)
            del info[0]
        else:
            max_prince = max(info)
            max_point = info.index(max_price)
            revenue += max_price * len(info[:max_point]) - sum(info[:max_point])
            del info[:max_point]

    print(f'#{case} {revenue}')