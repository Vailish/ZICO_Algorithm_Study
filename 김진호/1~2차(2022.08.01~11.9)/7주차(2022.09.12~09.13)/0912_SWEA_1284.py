for test_case in range(1,int(input())+1):
    P, Q, R, S, W = map(int,input().split())        # 문제에서 주어진 그대로 입력받음
    a_pay = W * P
    b_pay = Q if W <= R else Q + (W - R) * S        # 기본요금 사용량보다 크고 작음 기준으로 계산식 변경
    print(f'#{test_case} {a_pay if a_pay <= b_pay else b_pay}')
